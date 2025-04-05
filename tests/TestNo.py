import re
from playwright.sync_api import Page, expect
from dotenv import load_dotenv
import os
import pytest
from faker import Faker

load_dotenv()
NUM_ADULTS = int(os.getenv("NUM_ADULTS"))
API_URL = os.getenv("API_URL")
fake = Faker()

@pytest.mark.parametrize("url", [API_URL])
def test_example(page: Page, url: str) -> None:
    #page 1 
    page.goto(url)
    page.click(".vuetable-body > tr:nth-child(1) > td:nth-child(6) > span:nth-child(1)")
    with page.expect_popup() as page1_info:
        page.click(".button")
    page1 = page1_info.value
    #page 2 
    page1.click(".btn")
    page1.locator(".radio-list-item").first.click()
    page1.locator("div:nth-child(12) > .radio-field > .mdt-radio-list > .radio-list > li").first.click()
    page1.locator("div:nth-child(13) > .radio-field > .mdt-radio-list > .radio-list > li").first.click()
    page1.locator("div:nth-child(15) > .radio-field > .mdt-radio-list > .radio-list > li").first.click()
    page1.locator("div:nth-child(18) > .radio-field > .mdt-radio-list > .radio-list > li").first.click()
    page1.locator("div:nth-child(21) > .radio-field > .mdt-radio-list > .radio-list > li").first.click()
    page1.locator("div:nth-child(24) > .radio-field > .mdt-radio-list > .radio-list > li").first.click()
    page1.locator("div:nth-child(26) > .radio-field > .mdt-radio-list > .radio-list > li").first.click()
    page1.locator("div:nth-child(27) > .radio-field > .mdt-radio-list > .radio-list > li").first.click()
    page1.locator("div:nth-child(29) > .radio-field > .mdt-radio-list > .radio-list > li").first.click()
    page1.click(".btn")
    
    
    page1.wait_for_load_state('networkidle')
    #page 3 
    page1.click("div.section:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    page1.click("li.dropdown-item:nth-child(1) > div:nth-child(1)")
    page1.click("div.section:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1)")
    page1.click("div.section:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(6) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1)")
    page1.click("div.section:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(8) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1)")
    page1.click("div.section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    page1.click("li.dropdown-item:nth-child(1) > div:nth-child(1)")
    page1.click("div.section:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1)")
    page1.click(".selected")
    page1.click("div.section:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    page1.click("li.dropdown-item:nth-child(1) > div:nth-child(1)")
    page1.click("div.btn:nth-child(2)")
        # ^^so far so good ^^
#page 4

    i = 1  # Start from 1 to ensure at least one iteration
    while i <= NUM_ADULTS:
        page1.click(".create-adult > div:nth-child(1)")
        page1.click(".nested-form-slot > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > i:nth-child(2)")
        page1.click("li.dropdown-item:nth-child(1) > div:nth-child(1)")      
        page1.fill(".nested-form-slot > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)", fake.first_name())
        page1.fill(".nested-form-slot > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)", fake.last_name())
        page1.get_by_role("textbox", name="DD.MM.YYYY").first.click()
        page1.get_by_role("textbox", name="DD.MM.YYYY").first.fill(fake.date_of_birth().strftime("%d.%m.%Y"))
        
        page1.click(".nested-form-slot > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
        page1.click("li.dropdown-item:nth-child(1) > div:nth-child(1)")
       
        page1.click(".nested-form-slot > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
        page1.click("li.dropdown-item:nth-child(1) > div:nth-child(1)")

        page1.click(".nested-form-slot > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(12) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > i:nth-child(2)")
        page1.click("li.dropdown-item:nth-child(1) > div:nth-child(1)")

        page1.locator("div:nth-child(9) > .mt-16 > .mdt-input > .input-wrapper > .text-cut").click()
        page1.locator("div:nth-child(9) > .mt-16 > .mdt-input > .input-wrapper > .text-cut").fill(fake.text())
        page1.fill("div.section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(2)",fake.numerify("78 ### ## ##"))
        
        fake_email = fake.email()
        page1.fill(".mdt-input-email-with-confirm > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)",fake_email)
        page1.locator("input[type=\"email\"]").first.fill(fake_email)
        page1.locator("input[type=\"email\"]").nth(1).click()
        page1.locator("input[type=\"email\"]").nth(1).fill(fake_email)
        page1.locator("div:nth-child(13) > .mt-16 > .mdt-input > .input-wrapper > .text-cut").click()
        page1.locator("div:nth-child(13) > .mt-16 > .mdt-input > .input-wrapper > .text-cut").fill(fake.text())
        page1.get_by_role("spinbutton").first.click()
        page1.get_by_role("spinbutton").first.fill("1")
        page1.locator("div:nth-child(15) > .mt-16 > .mdt-input > .input-wrapper > .text-cut").click()
        page1.locator("div:nth-child(15) > .mt-16 > .mdt-input > .input-wrapper > .text-cut").fill(fake.text())


        page1.click("div.section:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(16) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > i:nth-child(2)")
        page1.click("li.dropdown-item:nth-child(1) > div:nth-child(1)")
        
        page1.get_by_role("textbox", name="DD.MM.YYYY").nth(2).click()
        page1.get_by_role("textbox", name="DD.MM.YYYY").nth(2).fill(fake.date_of_birth().strftime("%d.%m.%Y"))
        
        page1.click("div.section:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > i:nth-child(2)")
        page1.click("li.dropdown-item:nth-child(1) > div:nth-child(1)")
        page1.click("div.mdt-radio-list:nth-child(2) > ul:nth-child(2) > li:nth-child(1)")
        page1.click("#agreement_references")
        page1.click(".btn-primary")

        i += 1

    page1.wait_for_timeout(1000)
    page1.wait_for_load_state('networkidle')
    page1.click(".btn-next")
    page1.wait_for_load_state('networkidle')

    #page 5 
    page1.click("#agreement_penalty")
    page1.click("#agreement_truth")
    page1.click("#agreement_privacy")
    page1.click("div.btn:nth-child(2)")