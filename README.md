# Smart-Lottery-System-

智能抽号系统
一个基于Python Tkinter开发的智能抽号工具，适用于课堂提问、班务分配等场景，支持多种抽号模式与安全管理功能。
主要功能：
	核心特性
		多模式抽号：支持英语背书、英语听写、心理活动等5种预设模式
		智能记录：自动记录历史抽号，避免重复抽取
		性别筛选：支持按男生/女生单独抽号
		爆率控制- 可设置特定号码的中签频率
		时间限制- 限制非授课时段使用
		权限管理- 区分普通用户和管理员权限
	安全特性
		配置文件加密存储
		操作日志记录
		密码认证（一次性密码）

使用指南：
	普通用户
		解锁系统默认密码：111111，可以从管理员界面导入
		在指定时间段内自动解锁
		选择操作模式，设置最大号码和抽取数量
		可选性别筛选（男女生信息自己到ConfigEngine里面改）
		数据导入：右键点击状态栏红点，通过密码验证后拖入TXT文件（每行一个数字）
	管理员
		进入面板：使用默认密码admin123解锁
		爆率调整：设置特定号码的中签频率
		密码管理：重置普通/管理员密码
		时间设置：修改禁用时间段
		记录管理：查看/清除历史数据

注意事项：
	首次使用请先用管理员密码（admin123)登录管理员账户并设置好不同的密码，管理员密码丢失将导致系统无法重置。定期备份ConfigEngine目录。


常见问题”
Q：无法在非授课时间使用？
A: 管理员可调整时间限制规则，首次使用前可根据操作时间在代码里修改。第一次修改后如果打开了程序修改代码无效
Q: 忘记管理员密码”
A: 手动删除PasswordVault/admin_passwords.enc文件后重新打开。

注意：本系统加密方案不适合高安全需求场景，重要数据请自行备份。首次运行将在python文件存放位置自动生成ConfigEngine配置目录。
结构：
ConfigEngine/
├── PasswordVault/       # 密码存储
├── RateSettings/        # 爆率配置
├── LotteryRecords/      # 抽号记录
└── TimeRestrictions/    # 时间限制


[read me用了deepseek帮我写^______^]


开发：Wong0728,哔哩哔哩UID:3546672074328639 | 版本：1.0 | 更新日期：2025/4/5
