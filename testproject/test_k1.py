# ## 1 Feladat: Pitagorasz-tétel
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
#
# A program töltse be a Pitagorasz-tétel app-ot az [https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html](https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a Pitagorasz-tétel appban:
#
# Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!
#
# * Helyesen jelenik meg az applikáció betöltéskor:
#     * a: <üres>
#     * b: <üres>
#     * c: <nem látszik>
#
# * Számítás helyes, megfelelő bemenettel
#     * a: 2
#     * b: 3
#     * c: 10
#
# * Üres kitöltés:
#     * a: <üres>
#     * b: <üres>
#     * c: NaN
#
# ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `k1.py`
# * a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
# * majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
# * ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
# * akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
# * a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
# * nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(
# 1 Feladat helye:

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from pprint import pprint
import csv
import time

def test_k1():
    # opt = Options()
    # opt.headless = False
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

    # In order for ChromeDriverManager to work you must pip install it in your own environment.
    driver = webdriver.Chrome(ChromeDriverManager().install())

    def pythagorasz(x, y, z):
        a_input = driver.find_element_by_id("a")
        a_input.clear()
        a_input.send_keys(x)
        time.sleep(1)
        b_input = driver.find_element_by_id("b")
        b_input.clear()
        b_input.send_keys(y)
        time.sleep(1)
        kalkulacio_button = driver.find_element_by_id("submit")
        kalkulacio_button.click()
        time.sleep(3)
        result = driver.find_element_by_id("result")
        print(z)
        print(result.text)
        assert result.text == z


    try:
        URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"
        driver.get(URL)
        time.sleep(5)

        # TC1
        # Helyesen jelenik meg az applikáció betöltéskor:
        #     * a: <üres>
        #     * b: <üres>
        #     * c: <nem látszik>
        assert driver.find_element_by_id("a").text == ''
        assert driver.find_element_by_id("b").text == ''
        assert driver.find_element_by_id("result").is_displayed() == False
        # pythagorasz('', '', '',)

        # TC2
        # Számítás helyes, megfelelő bemenettel
        #     * a: 2
        #     * b: 3
        #     * c: 10
        pythagorasz('2', 3, '10')

        # TC3
        # * Üres kitöltés:
        #     * a: <üres>
        #     * b: <üres>
        #     * Eredmény: NaN
        pythagorasz('', '', 'NaN')

    except NoSuchElementException as exc:
        print("Hiba történt: ", exc)

    finally:
        #pass
        driver.close()
        driver.quit()
