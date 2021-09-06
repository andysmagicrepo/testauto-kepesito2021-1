## 4 Feladat: Műveletek karakterekkel
#
# Készíts egy Python python applikációt(egy darab python file) ami selenium - ot használ.
#
# A program töltse be a Műveletek karakterekkel app - ot
# az[https: // ambitious - sky - 0
# d3acbd03.azurestaticapps.net / k4.html](https: // ambitious-sky-0d3acbd03.azurestaticapps.net / k4.html)
# oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel a Műveletek karakterekkel app tesztelését.
#
# Az applikáció minden frissítésnél véletlenszerűen változik!
# Az ellenőrzésekhez használj `pytest` keretrendszert.A tesztjeidben használj
# `assert ` összehasonlításokat használj!
#
# Az alábbi teszt eseteket kell kidolgozzad:
#
# *Helyesen betöltődik az applikáció: \
#     *Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
#     * !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
#
# *Megjelenik egy érvényes művelet:
# *`chr` megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
# *`op` mező vagy + vagy - karaktert tartlamaz
# *`num` mező egy egész számot tartalamaz
#
# *Gombnyomásra helyesen végződik el a random művelet a fenti ABCs tábla alapján:
#     *A megjelenő `chr` mezőben lévő karaktert kikeresve a táblában \
#     *Ha a `+` művelet jelenik meg akkor balra lépve ha a `-` akkor jobbra lépve \
#     *A `num` mezőben megjelenő mennyiségű karaktert
#     *az `result` mező helyes karaktert fog mutatni
# ### A megoldás beadása
# *a megoldásokat a `testproject` mappába tedd, `k4.py`
# *a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
# *majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni \
# *ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása(`ctlr` + `alt` + `l`)
# *akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
# *a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni.Ne vidd túlzásba, de ne is legyen
# komment nélkül leadott fájlod.
# *nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér: (
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from pprint import pprint
import csv
import time

def test_k4():
    # opt = Options()
    # opt.headless = False
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

    # In order for ChromeDriverManager to work you must pip install it in your own environment.
    driver = webdriver.Chrome(ChromeDriverManager().install())

    try:
        URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"
        driver.get(URL)
        time.sleep(5)

        szoveg = driver.find_element_by_xpath('/html/body/div/div/p[3]').text
        print(szoveg)
        kell = '!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{ |}~'
        assert szoveg == kell
        jo = 0
        opmezo = driver.find_element_by_id('op')
        if opmezo == '+' or opmezo == '-':
            jo = 1
        assert jo == 1
        nummezo = driver.find_element_by_id('num')
        jon = 0
        if int(nummezo) == nummezo:
            jon = 1
        assert jon == 1


    except NoSuchElementException as exc:
        print("Hiba történt: ", exc)

    finally:
        driver.close()
        driver.quit()