import re
from playwright.sync_api import Page, expect
from dotenv import load_dotenv
import os
import pytest
from faker import Faker

load_dotenv()

API_URL = os.getenv("API_URL")
fake = Faker()

@pytest.mark.parametrize("url", [API_URL])
def test_example(page: Page, url: str) -> None:
    page.goto(url)
    page.get_by_role("row", name="00.01.02 Kanzlei A CHF 1'850").locator("i").click()
    with page.expect_popup() as page1_info:
        page.get_by_text("Apply").click()
    page1 = page1_info.value
    page1.get_by_text("Start").click()
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
    page1.get_by_text("Save and next").click()
    
    
    page1.wait_for_load_state('networkidle')
    
    page1.get_by_role("textbox", name="Please choose").first.click()
    page1.get_by_text("single person household").click()
    page1.get_by_role("listitem", name="No").first.click()
    page1.get_by_role("listitem", name="No").nth(1).click()
    page1.get_by_role("listitem", name="No").nth(2).click()
    page1.get_by_role("textbox", name="Please choose").nth(1).click()
    page1.get_by_text("Reconstruction/Renovation").click()
    page1.get_by_role("listitem", name="Security deposit").click()
    page1.get_by_role("listitem", name="No").nth(3).click()
    page1.get_by_role("textbox", name="Please choose").nth(2).click()
    page1.get_by_text("Instagram").click()
    page1.get_by_text("Save and next").click()
    page1.get_by_text("Add adult").click()
    page1.locator(".text-cut").first.click()
    page1.get_by_text("Mr.").click()
    page1.get_by_role("textbox", name="Please specify").first.click()
    page1.get_by_role("textbox", name="Please specify").first.fill(fake.name())
    page1.get_by_role("textbox", name="Please specify").nth(1).click()
    page1.get_by_role("textbox", name="Please specify").nth(1).fill(fake.name())
    page1.get_by_role("textbox", name="DD.MM.YYYY").first.click()
    page1.get_by_role("cell", name="11").click()
    page1.locator("div:nth-child(7) > .mt-16 > div > .mdt-select > .select-wrapper > .search > .mdt-input > .input-wrapper > .text-cut").click()
    page1.get_by_text("married").click()
    page1.get_by_role("textbox", name="Search...").first.click()
    page1.get_by_text("Switzerland", exact=True).click()
    page1.locator("div:nth-child(9) > .mt-16 > .mdt-input > .input-wrapper > .text-cut").click()
    page1.locator("div:nth-child(9) > .mt-16 > .mdt-input > .input-wrapper > .text-cut").fill(fake.text())
    page1.get_by_role("textbox", name="Please choose").nth(2).click()
    page1.get_by_text("Spouse, registered partnership").click()
    page1.get_by_role("textbox", name="123 45 67").first.click()
    page1.get_by_role("textbox", name="123 45 67").first.fill(fake.numerify("78 ### ## ##"))
    page1.get_by_role("textbox", name="123 45 67").nth(1).click()
    page1.get_by_role("textbox", name="123 45 67").nth(1).fill(fake.numerify("78 ### ## ##"))
    page1.locator("input[type=\"email\"]").first.click()
    fake_email = fake.email()
    page1.locator("input[type=\"email\"]").first.fill(fake_email)
    page1.locator("input[type=\"email\"]").nth(1).click()
    page1.locator("input[type=\"email\"]").nth(1).fill(fake_email)
    page1.locator("div:nth-child(13) > .mt-16 > .mdt-input > .input-wrapper > .text-cut").click()
    page1.locator("div:nth-child(13) > .mt-16 > .mdt-input > .input-wrapper > .text-cut").fill(fake.text())
    page1.get_by_role("spinbutton").first.click()
    page1.get_by_role("spinbutton").first.fill("1")
    page1.locator("div:nth-child(15) > .mt-16 > .mdt-input > .input-wrapper > .text-cut").click()
    page1.locator("div:nth-child(15) > .mt-16 > .mdt-input > .input-wrapper > .text-cut").fill(fake.text())
    page1.get_by_role("textbox", name="Search...").nth(1).click()
    page1.get_by_text("Switzerland", exact=True).click()
    page1.get_by_role("textbox", name="DD.MM.YYYY").nth(2).click()
    page1.get_by_role("cell", name="11").click()
    page1.get_by_role("listitem", name="No").first.click()
    page1.get_by_role("listitem", name="No").nth(1).click()
    page1.get_by_role("listitem", name="No").nth(2).click()
    page1.get_by_role("textbox", name="Please choose").nth(4).click()
    page1.get_by_text("Unemployed", exact=True).click()
    page1.get_by_role("listitem", name="CreditTrust certificate").click()
    page1.get_by_role("checkbox", name="I hereby confirm that").check()
    page1.get_by_text("Save", exact=True).click()
    page1.wait_for_timeout(1000)
    page1.wait_for_load_state('networkidle')
    page1.get_by_text("Save and next").click(force=True)
    page1.wait_for_load_state('networkidle')
    page1.get_by_role("checkbox", name="Should the prospective tenant").check(force=True)
    page1.get_by_role("checkbox", name="I confirm that I have").check(force=True)
    page1.get_by_role("checkbox", name="I have read the privacy").check(force=True)
    page1.get_by_text("Save").click()