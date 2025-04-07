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
    #pg1
    page.goto(url)
    page.click(".vuetable-body > tr:nth-child(1) > td:nth-child(6) > span:nth-child(1)")
    with page.expect_popup() as page1_info:
        page.click(".button")
    page2 = page1_info.value

    #pg2
    page2.click(".btn")
    page2.locator(".radio-list-item").first.click()
    page2.locator("div:nth-child(12) > .radio-field > .mdt-radio-list > .radio-list > li").first.click()
    page2.locator("div:nth-child(13) > .radio-field > .mdt-radio-list > .radio-list > li").first.click()
    page2.locator("div:nth-child(15) > .radio-field > .mdt-radio-list > .radio-list > li").first.click()
    page2.locator("div:nth-child(18) > .radio-field > .mdt-radio-list > .radio-list > li").first.click()
    page2.locator("div:nth-child(21) > .radio-field > .mdt-radio-list > .radio-list > li").first.click()
    page2.locator("div:nth-child(24) > .radio-field > .mdt-radio-list > .radio-list > li").first.click()
    page2.locator("div:nth-child(26) > .radio-field > .mdt-radio-list > .radio-list > li").first.click()
    page2.locator("div:nth-child(27) > .radio-field > .mdt-radio-list > .radio-list > li").first.click()
    page2.locator("div:nth-child(29) > .radio-field > .mdt-radio-list > .radio-list > li").first.click()
    page2.click(".btn")
    
    
    page2.wait_for_load_state('networkidle')
    
    
        
    #pg3
    page2.click("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.navigation-buttons > div.btn.btn-next")
    expect(page2.locator(".client-errors").first).to_be_visible()
    expect(page2.locator(".mdt-radio-list > .input-errors > .client-errors").first).to_be_visible()
    expect(page2.locator("div:nth-child(6) > .radio-field > .mdt-radio-list > .input-errors > .client-errors")).to_be_visible()
    expect(page2.locator("div:nth-child(2) > div > div > div:nth-child(2) > .mt-16 > div > .mdt-select > .input-errors > .client-errors")).to_be_visible()
    expect(page2.locator("div:nth-child(2) > .radio-field > .mdt-radio-list > .input-errors > .client-errors")).to_be_visible()
    expect(page2.locator("div:nth-child(5) > div > div > div:nth-child(2) > .mt-16 > div > .mdt-select > .input-errors > .client-errors")).to_be_visible()
    
    page2.click("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.application-form > div > div > div:nth-child(1) > div > div > div:nth-child(2) > div > div > div > div.select-wrapper > div > div")
    page2.click("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.application-form > div > div > div:nth-child(1) > div > div > div:nth-child(2) > div > div > div > div.select-wrapper.focused > div.select-dropdown.bottom > div > div.__panel > div > ul > li:nth-child(3) > div")   

    page2.click("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.application-form > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > div > ul > li:nth-child(1)")
    page2.click("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.application-form > div > div > div:nth-child(1) > div > div > div:nth-child(6) > div > div > ul > li:nth-child(1)")

    page2.click("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.application-form > div > div > div:nth-child(2) > div > div > div:nth-child(2) > div > div > div > div.select-wrapper > div > div")
    page2.click("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.application-form > div > div > div:nth-child(2) > div > div > div:nth-child(2) > div > div > div > div.select-wrapper.focused > div.select-dropdown.bottom > div > div.__panel > div > ul > li:nth-child(1) > div")

    page2.click("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.application-form > div > div > div:nth-child(3) > div > div > div:nth-child(2) > div > div > ul > li:nth-child(1)")

    page2.click("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.application-form > div > div > div:nth-child(5) > div > div > div:nth-child(2) > div > div > div > div.select-wrapper > div > div")
    page2.click("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.application-form > div > div > div:nth-child(5) > div > div > div:nth-child(2) > div > div > div > div.select-wrapper.focused > div.select-dropdown.bottom > div > div.__panel > div > ul > li:nth-child(1) > div")
     
    page2.click("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.navigation-buttons > div.btn.btn-next")
    

    #pg4    
    '''
    Ne znam zasto ali stranica nekad izbaci error kao admin_error_saving_data pa to bricka citav proces
    admin_error.JPG

    '''
    page2.wait_for_load_state('networkidle')
    expect(page2.locator("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.navigation-buttons > div.btn.btn-next")).to_be_visible()
    page2.wait_for_load_state('networkidle')
    page2.wait_for_timeout(1000)
    page2.click("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.navigation-buttons > div.btn.btn-next")
    page2.wait_for_load_state('networkidle')
    page2.wait_for_selector("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.navigation-buttons > div.btn.btn-next")
    expect(page2.locator("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.application-form > div > div > div > div > div > div:nth-child(4) > div > div:nth-child(2) > div > div > div.has-error")).to_be_visible()
    
    expect(page2.locator("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.application-form > div > div > div > div > div > div:nth-child(3) > div > div:nth-child(2) > div.create-person.has-error > div > div.has-error")).to_be_visible()
    page2.wait_for_load_state('networkidle')
    expect(page2.locator("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.application-form > div > div > div > div > div > div:nth-child(3) > div > div:nth-child(2) > div.create-person.has-error > div > div.has-error")).to_be_visible()
    page2.locator("i").nth(3).click()
    page2.wait_for_timeout(2000)
    page2.click("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.application-form > div.nested-form-slot > div > div.nested-buttons > div.btn.btn-primary")
    page2.wait_for_timeout(2000)
    
    expect(page2.locator(".client-errors").first).to_be_visible()
    
    expect(page2.locator(".mdt-input > .input-errors > .client-errors").first).to_be_visible()
    expect(page2.locator("div:nth-child(4) > .mt-16 > .mdt-input > .input-errors > .client-errors")).to_be_visible()
    expect(page2.locator(".datepicker-input > .mdt-input > .input-errors > .client-errors").first).to_be_visible()
    expect(page2.locator("div:nth-child(7) > .mt-16 > div > .mdt-select > .input-errors > .client-errors")).to_be_visible()
    expect(page2.locator(".mt-16 > .mdt-select > .input-errors > .client-errors").first).to_be_visible()
    expect(page2.locator("div:nth-child(10) > .mt-16 > div > .mdt-select > .input-errors > .client-errors")).to_be_visible()
    expect(page2.locator("div:nth-child(12) > .mt-16 > div > .mdt-select > .input-errors > .client-errors")).to_be_visible()
    expect(page2.locator(".mdt-phone-number-input > .input-errors > .client-errors")).to_be_visible()
    expect(page2.locator(".mdt-input-email-with-confirm > div > .input-errors > .client-errors").first).to_be_visible()
    expect(page2.locator("div:nth-child(2) > .input-errors > .client-errors").first).to_be_visible()
    expect(page2.locator("div:nth-child(13) > .mt-16 > .mdt-input > .input-errors > .client-errors")).to_be_visible()
    expect(page2.locator("div:nth-child(14) > .mt-16 > div > .mdt-input > .input-errors > .client-errors")).to_be_visible()
    expect(page2.locator("div:nth-child(15) > .mt-16 > .mdt-input > .input-errors > .client-errors")).to_be_visible()
    expect(page2.locator("div:nth-child(16) > .mt-16 > .mdt-select > .input-errors > .client-errors")).to_be_visible()
    expect(page2.locator("div:nth-child(17) > .mt-16 > .mdt-datepicker > .datepicker-input > .mdt-input > .input-errors > .client-errors")).to_be_visible()
    expect(page2.locator("div:nth-child(3) > .mt-16 > div > .mdt-select > .input-errors > .client-errors")).to_be_visible()
    expect(page2.locator(".mdt-radio-list > .input-errors > .client-errors")).to_be_visible()
    expect(page2.locator(".mdt-checkbox > .input-errors > .client-errors")).to_be_visible()

    page2.click(".nested-form-slot > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > i:nth-child(2)")
    page2.click("li.dropdown-item:nth-child(1) > div:nth-child(1)")      
    page2.fill(".nested-form-slot > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)", fake.first_name())
    page2.fill(".nested-form-slot > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)", fake.last_name())
    page2.get_by_role("textbox", name="DD.MM.YYYY").first.click()
    page2.get_by_role("textbox", name="DD.MM.YYYY").first.fill(fake.date_of_birth().strftime("%d.%m.%Y"))
    
    page2.click(".nested-form-slot > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    page2.click("li.dropdown-item:nth-child(1) > div:nth-child(1)")
    
    page2.click(".nested-form-slot > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    page2.click("li.dropdown-item:nth-child(1) > div:nth-child(1)")

    page2.click(".nested-form-slot > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(12) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > i:nth-child(2)")
    page2.click("li.dropdown-item:nth-child(1) > div:nth-child(1)")

    page2.locator("div:nth-child(9) > .mt-16 > .mdt-input > .input-wrapper > .text-cut").click()
    page2.locator("div:nth-child(9) > .mt-16 > .mdt-input > .input-wrapper > .text-cut").fill(fake.text())
    page2.fill("div.section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(2)",fake.numerify("78 ### ## ##"))
    
    fake_email = fake.email()
    page2.fill(".mdt-input-email-with-confirm > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)",fake_email)
    page2.locator("input[type=\"email\"]").first.fill(fake_email)
    page2.locator("input[type=\"email\"]").nth(1).click()
    page2.locator("input[type=\"email\"]").nth(1).fill(fake_email)
    page2.locator("div:nth-child(13) > .mt-16 > .mdt-input > .input-wrapper > .text-cut").click()
    page2.locator("div:nth-child(13) > .mt-16 > .mdt-input > .input-wrapper > .text-cut").fill(fake.text())
    page2.get_by_role("spinbutton").first.click()
    page2.get_by_role("spinbutton").first.fill("1")
    page2.locator("div:nth-child(15) > .mt-16 > .mdt-input > .input-wrapper > .text-cut").click()
    page2.locator("div:nth-child(15) > .mt-16 > .mdt-input > .input-wrapper > .text-cut").fill(fake.text())


    page2.click("div.section:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(16) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > i:nth-child(2)")
    page2.click("li.dropdown-item:nth-child(1) > div:nth-child(1)")
    
    page2.get_by_role("textbox", name="DD.MM.YYYY").nth(2).click()
    page2.get_by_role("textbox", name="DD.MM.YYYY").nth(2).fill(fake.date_of_birth().strftime("%d.%m.%Y"))
  

    page2.click("div.section:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > i:nth-child(2)")
    page2.click("li.dropdown-item:nth-child(1) > div:nth-child(1)")
    page2.click("div.mdt-radio-list:nth-child(2) > ul:nth-child(2) > li:nth-child(1)")
    page2.click("#agreement_references")
    page2.click(".btn-primary")

    page2.wait_for_timeout(2000)
    page2.click("div.btn:nth-child(2)")
    
    expect(page2.locator("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.application-form > div > div > div > div > div > div:nth-child(4) > div > div:nth-child(2) > div > div > div.has-error")).to_be_visible()

    page2.click("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.application-form > div > div > div > div > div > div:nth-child(4) > div > div:nth-child(2) > div > div > div.container")
    page2.click(".btn-primary")
    expect(page2.locator(".nested-form-slot > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)")).to_be_visible()
    expect(page2.locator(".nested-form-slot > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)")).to_be_visible()
    expect(page2.locator(".datepicker-input > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)")).to_be_visible()
    expect(page2.locator(".mdt-number-incrementer > div:nth-child(3) > span:nth-child(1)")).to_be_visible()

    page2.fill(".nested-form-slot > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)", fake.first_name())
    page2.fill(".nested-form-slot > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)", fake.last_name())
    page2.fill(".has-icon > input:nth-child(1)",fake.date_of_birth().strftime("%d.%m.%Y"))
    page2.click(".fa-caret-down")
    page2.click("li.dropdown-item:nth-child(2) > div:nth-child(1)")
    page2.click(".fa-plus")
    page2.click(".btn-primary")



    page2.wait_for_timeout(1000)
    page2.wait_for_load_state('networkidle')
    page2.click(".btn-next")
    page2.wait_for_load_state('networkidle')
    #pg5
    expect(page2.locator("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.navigation-buttons > div.btn.btn-next")).to_be_visible()
    page2.wait_for_timeout(1000)
    page2.wait_for_load_state('networkidle')
   
    page2.click("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.navigation-buttons > div.btn.btn-next")
    expect(page2.locator("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.application-form > div > div > div:nth-child(4) > div > div > div:nth-child(2) > div > div > div > div.input-errors > span")).to_be_visible()
    expect(page2.locator("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.application-form > div > div > div:nth-child(4) > div > div > div:nth-child(3) > div > div > div > div.input-errors > span")).to_be_visible()
    expect(page2.locator("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.application-form > div > div > div:nth-child(4) > div > div > div:nth-child(4) > div > div > div > div.input-errors > span")).to_be_visible()
    page2.wait_for_timeout(1000)
    page2.wait_for_load_state('networkidle')
    page2.click("body > div > div > div.application-form > div.application-form-container > div.content > div:nth-child(2) > div.navigation-buttons > div.btn.btn-next")
    