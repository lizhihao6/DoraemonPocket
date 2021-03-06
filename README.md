# Python Package Template

ð¦ ä¸ä¸ªå¿«éä¸ä¼ å° PyPI ç Python Package æ¨¡çã

> ä¸ä¼ å° PyPI åå¯ä»¥ä½¿ç¨ pip install å®è£ã

## 1 ä½¿ç¨æ¹æ³

1. ç¹å»æ¬é¡¹ç®å³ä¸è§çç»¿è²æé® `Use this template`ï¼ä½¿ç¨æ­¤æ¨¡æ¿ï¼ï¼è¾å¥åç§°åè¯´æï¼å®æåå»ºï¼

2. å°é¡¹ç®åéå°æ¬å°ï¼è¿éä»¥æ¬é¡¹ç®ä¸ºä¾ï¼å®éæä½æ¶è¿ééè¦æ¿æ¢ä½ èªå·±çé¡¹ç®ï¼

    ```bash
    git clone https://github.com/Ailln/python-package-template.git --depth 1
    ```

3. ä¿®æ¹éç½®ï¼æä»¶ä¸­ææç¤ºï¼

    ```bash
    cd python-package-template

    # 1. å°ä¸æä¸­ç your_package_name æ¹æä½ çå®éé¡¹ç®åç§°
    mv package_name your_package_name

    # 2. æ¥ä¸æ¥ä¿®æ¹ `setup.py /package_name/shell/usage.py` ä¸­çåæ°ï¼éé¢ææç¤ºã

    # 3. æå `README.md` ä¿®æ¹ä¸ºä½ çé¡¹ç®ä»ç»ï¼ä¹å°±æ¯ä½ å½åå¨è¯»çè¿ä¸ªææ¬ã
    ```

4. ç¼åä½ ç Package ä»£ç ï¼

5. ä¸ä¼ å° PyPiï¼éè¦æ³¨åï¼ï¼åè[å¦ä½åå¸èªå·±çåå° pypi](https://www.v2ai.cn/2018/07/30/python/1-pypi/)ï¼

    ```bash
    bash scripts/upload_pypi.sh
    ```

6. æ´æ°å° Githubã

    ```bash
    git push
    ```

## 2 é¡¹ç®ç»æ

```
.
âââ README.md # é¡¹ç®ææ¡£
âââ package_name # ä½ éè¦æå¨ä¿®æ¹ä¸ºä½ çé¡¹ç®åç§°
â    âââ shell # å¨å½ä»¤è¡ä¸­æ§è¡çä»£ç 
â    â    âââ __init__.py
â    â    âââ usage.py
â    âââ src # éæèµæº
â    â    âââ temp.txt
â    âââ version.py # çæ¬å·
âââ scripts
â    âââ local_install.sh
â    âââ upload_pypi.sh
âââ requirements.txt # åä¾èµ
âââ .gitignore
âââ LICENSE # è¿éé¢çåå®¹ä¸ºæ¬é¡¹ç®ç Licenseï¼ä½ éè¦æå¨æ¿æ¢å®ã
âââ setup.py # å®è£éç½®
```

## 3 TODO

- [ ] å¢å èªå¨ä¿®æ¹ `package name` çèæ¬ã
- [ ] å¢å  test ç¸å³ä»£ç ã

## 4 è®¸å¯

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)

## 5 åè

- [å¦ä½ä»æ¨¡æ¿åå»ºä»åºï¼](https://docs.github.com/cn/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template)
- [å¦ä½åå¸èªå·±çåå° pypi ï¼](https://www.v2ai.cn/2018/07/30/python/1-pypi/)
