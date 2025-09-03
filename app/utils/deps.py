from __future__ import annotations

import importlib
import os
import subprocess
import sys


def ensure_package(package_name: str, default_version: str) -> None:
    """Ensure ``package_name`` is installed.

    If the package is missing, the user is prompted (or environment variable
    ``INSTALL_MISSING_DEPS`` controls behaviour) to install either the default
    compatible version, the latest release, a custom version, or abort.
    """

    try:
        importlib.import_module(package_name)
        return
    except ImportError:
        pass

    strategy = os.getenv("INSTALL_MISSING_DEPS")
    choice = None
    if strategy:
        strategy = strategy.lower()
        mapping = {
            "default": "d",
            "latest": "l",
            "custom": "c",
            "none": "n",
        }
        choice = mapping.get(strategy)

    if choice is None:
        if not sys.stdin.isatty():
            choice = "n"
        else:
            prompt = (
                f"Package '{package_name}' is required but not installed.\n"
                f"Install default version ({package_name}=={default_version}) [d], "
                "latest [l], custom [c], or abort [n]? "
            )
            choice = input(prompt).strip().lower() or "d"

    if choice == "n":
        raise RuntimeError(
            f"缺少依赖包 '{package_name}'。设置 INSTALL_MISSING_DEPS 以自动安装。"
        )

    if choice == "c":
        version = os.getenv("MISSING_DEPS_VERSION")
        if version is None:
            if sys.stdin.isatty():
                version = input("请输入安装版本号: ").strip()
            else:
                raise RuntimeError(
                    "自定义安装版本但未设置 MISSING_DEPS_VERSION 环境变量"
                )
        install_target = f"{package_name}=={version}"
    elif choice == "d":
        install_target = f"{package_name}=={default_version}"
    else:  # latest
        install_target = package_name

    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", install_target]
        )
    except Exception as exc:  # pragma: no cover - network dependent
        raise RuntimeError(
            f"自动安装失败，请检查网络或手动安装包: {package_name}"
        ) from exc

    importlib.invalidate_caches()
    try:
        importlib.import_module(package_name)
    except Exception as exc:  # pragma: no cover
        raise RuntimeError(f"安装 {package_name} 后导入失败: {exc}") from exc
