import solvers
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

interactive = True
driver = webdriver.Firefox()
driver.get("https://edublend.ucll.be/MBI24A/Exercise/Question/169165")

def main():
    elem = driver.find_element_by_id("Username")
    elem.clear()
    elem.send_keys("r0599128")
    elem = driver.find_element_by_id("Password")
    elem.clear()
    elem.send_keys("kakmetpiS1")
    elem.send_keys(Keys.RETURN)
    if interactive: input()

    while True:
        # elem = driver.find_element_by_css_selector(".question-content > p:nth-child(4)")
        answer(driver.page_source)
        try:
            success = driver.find_element_by_class_name("alert-succes")
            fail = driver.find_element_by_class_name("alert-succes")
        except Exception as e:
            print(e)
        if interactive: input()
        elem = driver.find_element_by_css_selector("a.mc-btn:nth-child(4)")
        elem.click()
    # driver.close()

questions = dict()
questions[re.compile("Gegeven netwerk (\d*)\.(\d*)\.(\d*)\.(\d*)/(\d*), geef het (\d*)e subnet waarin je minstens (\d*) hosts uniek kan adresseren.")] = solvers.A
questions[re.compile("Gegeven netwerk (\d*)\.(\d*)\.(\d*)\.(\d*)/(\d*), bereken het netmask.")] = solvers.B
questions[re.compile("Gegeven netwerk (\d*)\.(\d*)\.(\d*)\.(\d*)/(\d*), bereken het maximaal aantal hosts dat een uniek IP-adres binnen dit netwerk kunnen krijgen.")] = solvers.C
questions[re.compile("Gegeven een subnet (\d*)\.(\d*)\.(\d*)\.(\d*)/(\d*), bereken de volgende adressen.")] = solvers.D
# NETWERKADRES;EERST BRUIKBARE ADRES;LAATST BRUIKBARE ADRES;BROADCAST-ADRES 

def answer(question):
    question = question.strip();
    # print(question)
    for question_regex in questions.keys():
        regex_match = question_regex.search(question)
        print(regex_match)
        if regex_match is not None:
            anwsers = questions[question_regex](regex_match.groups())
            break
    if type(anwsers) is not list:
        elem = driver.find_element_by_id("StudentAnswer")
        elem.clear()
        elem.send_keys(anwsers)
        elem.send_keys(Keys.RETURN)
    else:
        netw_address = driver.find_element_by_id("NetworkAddressStudent")
        first_address = driver.find_element_by_id("FirstUsableAddressStudent")
        last_address = driver.find_element_by_id("LastUsableAddressStudent")
        broad_address = driver.find_element_by_id("BroadcastAddressStudent")
        netw_address.clear()
        netw_address.send_keys(anwsers[0])
        first_address.clear()
        first_address.send_keys(anwsers[1])
        last_address.clear()
        last_address.send_keys(anwsers[2])
        broad_address.clear()
        broad_address.send_keys(anwsers[3])
        broad_address.send_keys(Keys.RETURN)

if __name__ == "__main__":
    main()
