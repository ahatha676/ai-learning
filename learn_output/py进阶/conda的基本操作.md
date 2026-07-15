Conda的基本命令主要围绕**环境管理**和**包管理**两大核心功能展开。

以下是按功能分类的常用命令速查表，建议收藏。

### 🏠 环境管理

环境是Conda的核心，它能让你为不同项目创建独立的“沙盒”，避免包版本冲突。

| 任务          | 命令示例                                          | 说明                                       |
| :---------- | :-------------------------------------------- | :--------------------------------------- |
| **创建环境**    | `conda create -n <env_name> python=3.9`       | 创建一个名为 `<env_name>` 的新环境，并指定Python版本。    |
| **激活/切换环境** | `conda activate <env_name>`                   | 激活并切换到名为 `<env_name>` 的环境。               |
| **退出当前环境**  | `conda deactivate`                            | 退出当前激活的环境，回到`base`环境。                    |
| **列出所有环境**  | `conda env list` 或 `conda info --envs`        | 查看所有Conda环境，当前激活的环境前会有`*`号标记。            |
| **删除环境**    | `conda remove -n <env_name> --all`            | 永久删除名为 `<env_name>` 的环境及其所有包。            |
| **克隆环境**    | `conda create --clone <old_env> -n <new_env>` | 基于现有环境 `<old_env>` 克隆出一个新环境 `<new_env>`。 |
| **导出环境**    | `conda env export > environment.yml`          | 将当前环境的包列表导出到`environment.yml`文件，用于分享或备份。 |
| **导入环境**    | `conda env create -f environment.yml`         | 根据`environment.yml`文件创建一个完全相同的环境。        |

### 📦 包管理

在激活的环境中，你可以使用以下命令管理包。

| 任务 | 命令示例 | 说明 |
| :--- | :--- | :--- |
| **搜索包** | `conda search <package_name>` | 在Anaconda仓库中搜索可用的包。 |
| **安装包** | `conda install <package_name>` | 安装指定的包。可以指定版本，如 `conda install numpy=1.19.5`。 |
| **安装特定版本Python** | `conda install python=3.8` | 在当前环境中安装指定版本的Python。 |
| **列出已安装的包** | `conda list` | 查看当前环境中所有已安装的包及其版本。 |
| **更新包** | `conda update <package_name>` | 将指定包更新到最新版本。 |
| **更新所有包** | `conda update --all` | 将当前环境中所有包更新到最新版本。 |
| **卸载包** | `conda uninstall <package_name>` | 从当前环境中卸载指定的包。 |

### ⚙️ Conda 自身管理

这些命令用于管理和配置Conda本身。

| 任务 | 命令示例 | 说明 |
| :--- | :--- | :--- |
| **查看版本** | `conda --version` | 显示当前安装的Conda版本号。 |
| **更新Conda** | `conda update conda` | 将Conda自身更新到最新版本。 |
| **查看配置** | `conda config --show` | 显示Conda当前的配置信息，如频道(channel)设置等。 |
| **添加频道** | `conda config --add channels <channel_url>` | 添加一个新的软件包下载频道，例如国内镜像源。 |
| **清理缓存** | `conda clean --all` | 清理未使用的包缓存和索引缓存，释放磁盘空间。 |

### ℹ️ 信息查询

| 任务 | 命令示例 | 说明 |
| :--- | :--- | :--- |
| **查看Conda信息** | `conda info` | 显示Conda的版本、默认环境路径、频道等详细信息。 |

### 🆘 获取帮助

| 任务 | 命令示例 | 说明 |
| :--- | :--- | :--- |
| **查看所有命令** | `conda --help` 或 `conda -h` | 列出所有可用的Conda命令。 |
| **查看特定命令帮助** | `conda <command> --help` | 查看特定命令的详细用法和参数，例如 `conda install --help`。 |

### 💡 实用技巧

*   **缩写**：常用的选项可以缩写，例如 `--name` 可缩写为 `-n`，`--envs` 可缩写为 `-e`。
*   **指定环境**：大多数命令都可以通过 `-n <env_name>` 参数来指定操作的目标环境，而不必先激活它。

总的来说，掌握`create`, `activate`, `install`, `list`, `update`, `remove`等命令，就能满足日常的大部分需求。