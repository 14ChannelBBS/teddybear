class Config():
    """
    Teddybearの設定管理ファイル。
    """

    nodeName:str = "14ちゃんねる (Teddybear公式インスタンス)"
    nodeDescription:str = ("Fediverse史上初、ActivityPub対応の匿名掲示板")
    nodeAdmins: list = [
        {
            "name": "nennneko5787",
            "email": "nennneko5787@14chan.jp"
        }
    ]
    maintainer: list = [
        {
            "name": "nennneko5787",
            "email": "nennneko5787@14chan.jp"
        }
    ]
    langs: list = [
        "ja",
        #"en",
        #"zh",
        #"ko",
        #"fr",
        #"de"
    ]
    tosUrl: str = "https://{url}/mod/tos"
    privacyPolicyUrl: str = "https://{url}/mod/privacy"
    impressumUrl: str = "https://nennneko5787.cloudfree.jp/"
    repositoryUrl: str = "https://github.com/14ChannelBBS/teddybear"