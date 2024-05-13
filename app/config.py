class Config():
    """
    Teddybearの設定管理ファイル。
    ほとんどNodeInfo用の設定ですが、一部ソフトウェアの動作に関する設定もあります
    """


    # 絶対に変更しないで
    softwareVersion: str = "2024.5.5-beta"
    # ください！変更したら殺める


    serverAddress: str = "beta.14chan.jp"

    openRegistrations: bool = True

    nodeName:str = "14ちゃんねるβ"
    nodeDescription:str = "Fediverse史上初、ActivityPub対応の匿名掲示板<br>\n(本サービスはβテストなので、壊れたり、予告なしにサービスを終了する場合がございます)"
    nodeAdmins: list = [
        {
            "name": "nennneko5787",
            "email": "nennneko5787@14chan.jp"
        }
    ]
    maintainer: list = {
        "name": "nennneko5787",
        "email": "nennneko5787@14chan.jp"
    }
    langs: list = [
        "ja",
        #"en",
        #"zh",
        #"ko",
        #"fr",
        #"de"
    ]
    tosUrl: str = f"https://{serverAddress}/mod/tos"
    privacyPolicyUrl: str = f"https://{serverAddress}/mod/privacy"
    impressumUrl: str = "https://nennneko5787.cloudfree.jp/"

    disableRegistration: bool = True
    disableLocalTimeline: bool = False
    disableGlobalTimeline: bool = False
    emailRequiredForSignup: bool = False

    # 改造してTurnstile以外をつけたいという方は、ぜひどうぞ
    # reCAPCHAは割れているみたいなんでやめたほうがいいです
    enableHcaptcha: bool = False
    enableRecaptcha: bool = False
    enableMcaptcha: bool = False
    enableTurnstile: bool = True

    # 本文の最大文字数
    # 無難に2048文字ぐらいでいいんじゃないですかね？
    maxNoteTextLength: int = 2048

    enableEmail: bool = True
    enableServiceWorker: bool = True

    # 名無し名
    # 非ログインユーザーはそもそも書き込めないのでこの設定は削除されたアカウント用と思ってもらって問題はない
    proxyAccountName: str = "ghost"
    themeColor: str = "#87cefa"