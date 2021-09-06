# ## 2 Feladat: Színes reakció
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
#
# A program töltse be a Színes reakció app-ot az [https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html](https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel a Színes reakció app tesztelését.
#
# Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!
#
# Az alábbi teszteseteket kell lefedned:
#
# * Helyesen jelenik meg az applikáció betöltéskor:
#     * Alapból egy random kiválasztott szín jelenik meg az `==` bal oldalanán. A jobb oldalon csak a `[  ]` szimbólum látszik.
#     <szín neve> [     ] == [     ]
#
# * El lehet indítani a játékot a `start` gommbal.
#     * Ha elindult a játék akkor a `stop` gombbal le lehet állítani.
#
# * Eltaláltam, vagy nem találtam el.
#     * Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le
#     amikor a bal és a jobb oldal ugyan azt a színt tartalmazza akkor a `Correct!` felirat jelenik meg.
#       ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az `Incorrect!` felirat kell megjelenjen.
#
# ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `k2.py`
# * a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
# * majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
# * ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
# * akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
# * a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
# * nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from pprint import pprint
import csv
import time
from random import randint
from time import sleep


def test_k2():
# opt = Options()
# opt.headless = False
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"
    driver.get(URL)
    time.sleep(5)

    randcol = driver.find_element_by_id('randomColor')
    randcolname = driver.find_element_by_id('randomColorName').get_attribute('value')
    testcolor = driver.find_element_by_id('testColor')
    testcolorname = driver.find_element_by_id('testColorName').get_attribute('value')
    startgomb = driver.find_element_by_id('start')
    stopgomb = driver.find_element_by_id('stop')
    eredm = driver.find_element_by_id('result')

    #TC1
   # Helyesen jelenik meg az applikáció betöltéskor:
   # *Alapból egy random kiválasztott szín jelenik meg az ` == ` bal oldalanán. A   jobb oldalon
   # csak   a  `[]`  szimbólum   látszik.
   # < szín neve > [] == []
    print("randcolorname:", randcolname)
    #assert not randcolname.text != ''


    #TC2
    #El lehet indítani a játékot a `start` gommbal.
    #* Ha elindult a játék akkor a `stop` gombbal le lehet állítani.
    startgomb.click()
    sleep(randint(1, 4))
    print("testcolor:", testcolor.get_attribute('value'))
    print("testcolorname:", testcolorname)
    assert not testcolor.text == ''
    assert not testcolorname == ''
    stopgomb.click()
    print("eredm:", eredm.text)
    assert not eredm == ''

    #TC3
    #correct or incorrect answ
    startgomb.click()
    sleep(randint(1, 4))
    stopgomb.click()
    print("randcolor:", randcolname)
    print("testcolor:", testcolorname)
    print("eredm:", eredm.text)
    if randcolname == testcolorname:
        assert eredm.text == 'Correct!'
    else:
        assert eredm.text == 'Incorrect!'

except NoSuchElementException as exc:
    print("Hiba történt: ", exc)

finally:
    #pass
    driver.close()
    driver.quit()