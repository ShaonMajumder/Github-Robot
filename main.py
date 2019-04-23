#-*- coding:utf-8 -*-
import sys
sys.path.append("../bot_utility/")
from bot_utility import *
import configparser

#credentials
config = configparser.ConfigParser()
config.readfp(codecs.open("../config.ini", "r", "utf8"))

#class github():
#	def __init__():


def github_login(browser):
	browser.get("https://github.com/")
	while True:
		try:
			wait = WebDriverWait(browser, 1)
			browser.find_element_by_link_text("Sign in").click()
			#sign_in = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[text()="Sign in"]')))
			break
		except NoSuchElementException:
			pass
		except TimeoutException:
			pass

	#sign_in.click
	browser.find_element_by_id("login_field").click()
	browser.find_element_by_id("login_field").clear()
	browser.find_element_by_id("login_field").send_keys(config['GITHUB']['email'])
	browser.find_element_by_id("password").click()
	browser.find_element_by_id("password").clear()
	browser.find_element_by_id("password").send_keys(config['GITHUB']['password'])
	browser.find_element_by_name("commit").click()
	save_cookies(browser)
	browser.close()

def gmail_login(browser):
	browser.get("https://gmail.com")
	while True:
		try:
			wait = WebDriverWait(browser, 1)
			username_box = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
			break
		except NoSuchElementException:
			pass
		except TimeoutException:
			pass

	username_box.click()
	username_box.clear()
	username_box.send_keys(configs['gmail_shaon_username'])
	username_box.send_keys(Keys.ENTER)

	while True:
		try:
			wait = WebDriverWait(browser, 1)
			password_box = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@name="password"]')))
			break
		except NoSuchElementException:
			pass
		except TimeoutException:
			pass

	password_box.clear()
	password_box.send_keys(configs['gmail_shaon_password'])
	password_box.send_keys(Keys.ENTER)

	save_cookies(browser)

def transfer_repository(browser,repo_name,new_owner):
	#Most Loved Feature for bulk moving
	#Will not work for repository forked from others
	load_cookies(browser)
	browser.get("https://github.com/");
	textBox = browser.find_element_by_xpath("(.//input[contains(@aria-label,'Find a repository') and @id='dashboard-repos-filter-left'])")
	textBox.clear()
	textBox.send_keys(repo_name)
	textBox.send_keys(Keys.ENTER)

	time.sleep(2)

	container = browser.find_element_by_xpath("(.//div[contains(@class,'js-repos-container')])")
	conts = container.find_elements_by_xpath('//li[@class="public source no-description"]')
	for con in conts:
		if con.get_attribute("style") == "":
			con.click()
			break
	
	browser.find_element_by_xpath('//a[contains(@class,"js-selected-navigation-item") and contains(@data-selected-links,"repo_settings")]').click()
	time.sleep(2)
	browser.find_element_by_xpath('//summary[text()="Transfer"]').click()
	time.sleep(2)
	browser.find_element_by_xpath('//input[@class="form-control" and @id="confirm_repository_name"]').send_keys(repo_name)
	browser.find_element_by_xpath('//input[@id="confirm_new_owner" and @class="form-control" and @name="new_owner"]').send_keys(new_owner)
	browser.find_element_by_xpath('//button[@type="submit" and @class="btn btn-block btn-danger" and text()="I understand, transfer this repository."]').click()
	


def create_repository(browser,repo_name):
	load_cookies(browser)
	browser.get("https://github.com/")
	browser.find_element_by_css_selector("svg.octicon.octicon-plus.float-left.mr-1.mt-1").click()
	browser.find_element_by_link_text("New repository").click()
	browser.find_element_by_id("repository_name").click()
	browser.find_element_by_id("repository_name").clear()
	
	browser.find_element_by_id("repository_name").send_keys(repo_name)
	time.sleep(1)
	browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Nothing to show'])[2]/following::button[1]").click()
	browser.find_element_by_css_selector("svg.octicon.octicon-clippy").click()			
	
	win32clipboard.OpenClipboard()
	repo_link = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()
	browser.close()
	return repo_link

def search_for_repo(browser,repo_name):
	"""
	while True:
		check if the page is stable else wait
	"""

	while True:
		try:
			#search for repo name
			wait = WebDriverWait(browser, 1)
			repo_page = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@itemprop="name codeRepository"][normalize-space(text()) and normalize-space(.)=\''+repo_name+'\']')))
			repo_page.click()
			return True
		except NoSuchElementException:
			print("Not Found searching for disabled next")

			try:
				#if not found check reached to last page
				wait = WebDriverWait(browser, 1)
				next_btn_disabled = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="disabled"][text()="Next"]')))
				#if reached to last page and not found return
				return False
			except NoSuchElementException:
				print("searching for next")
				#if not found and not reached to last page, then next
				try:
					wait = WebDriverWait(browser, 1)
					next_btn = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@rel="nofollow"][text()="Next"]')))
					next_btn.click()
				except NoSuchElementException:
					pass
				except TimeoutException:
					pass
			except TimeoutException:
				print("searching for next")
				#if not found and not reached to last page, then next
				try:
					wait = WebDriverWait(browser, 1)
					next_btn = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@rel="nofollow"][text()="Next"]')))
					next_btn.click()
				except NoSuchElementException:
					pass
				except TimeoutException:
					pass
			
		except TimeoutException:
			print("Not Found searching for disabled next")

			try:
				#if not found check reached to last page
				wait = WebDriverWait(browser, 1)
				next_btn_disabled = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="disabled"][text()="Next"]')))
				#if reached to last page and not found return
				return False
			except NoSuchElementException:
				print("searching for next")
				#if not found and not reached to last page, then next
				try:
					wait = WebDriverWait(browser, 1)
					next_btn = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@rel="nofollow"][text()="Next"]')))
					next_btn.click()
				except NoSuchElementException:
					pass
				except TimeoutException:
					pass
			except TimeoutException:
				print("searching for next")
				#if not found and not reached to last page, then next
				try:
					wait = WebDriverWait(browser, 1)
					next_btn = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@rel="nofollow"][text()="Next"]')))
					next_btn.click()
				except NoSuchElementException:
					pass
				except TimeoutException:
					pass


def delete_repository(browser,repo_name):
	load_cookies(browser)
	browser.get("https://github.com/")
	browser.find_element_by_xpath('//summary[@aria-label="View profile and more"]').click()
	browser.find_element_by_link_text("Your repositories").click()
	
	if(search_for_repo(browser,repo_name)):
		pass
	else:
		print("Repository does not exist or cannot found.")
		return False

	#setting click
	browser.find_element_by_xpath('//a[@class="js-selected-navigation-item reponav-item"][contains(@data-selected-links,\'repo_settings repo_branch_settings\')]').click()

	#delete click
	while True:
		try:
			browser.find_element_by_xpath('//summary[@class="btn btn-danger boxed-action"][@aria-haspopup="dialog"][normalize-space(text()) and normalize-space(.)=\'Delete this repository\']').click()
			break
		except NoSuchElementException:
			pass
	
	#type in input verify repo_name
	while True:
		try:
			input_verify = browser.find_element_by_xpath('//input[@type="text"][@aria-label="Type in the name of the repository to confirm that you want to delete this repository."][@name="verify"]')
			break
		except NoSuchElementException:
			pass
	
	input_verify.clear()
	input_verify.send_keys(repo_name)

	#delete this repository
	browser.find_element_by_xpath('//button[@type="submit"][@class="btn btn-block btn-danger"][text()="I understand the consequences, delete this repository"]').click()
	browser.close()

def github():
	
	browser = get_webdriver({'image':'no','cache':'yes','UI':'yes'})
	github_login(browser)
	browser = get_webdriver({'image':'no','cache':'yes','UI':'yes'})

	repos = ['RML']
	for repo_name in repos:
		transfer_repository(browser,repo_name,"shaon-data")
def github2():
	repo_name = "shaon_boss"
	browser = get_webdriver({'image':'no','cache':'yes','UI':'yes'})
	github_login(browser)
	browser = get_webdriver({'image':'no','cache':'yes','UI':'yes'})
	print(create_repository(browser,repo_name))
	browser = get_webdriver({'image':'no','cache':'yes','UI':'yes'})
	delete_repository(browser,repo_name)
	quit()


def command_line():
	arguments = sys.argv
	if(query_yes_no("Are sure want to login github?")):
		browser = get_webdriver({'image':'no','cache':'yes','UI':'yes'})
		github_login(browser)

	if(len(arguments)>1):
		if(len(arguments) == 3):

			repo_name = arguments[2]
			
			if arguments[1] == "create_repo":
				if(query_yes_no("Are sure to create repositoy '"+repo_name+"'?")):
					browser = get_webdriver({'image':'no','cache':'yes','UI':'yes'})
					print(create_repository(browser,repo_name))
				else:
					print("exiting")
			elif arguments[1] == "delete_repo":
				if(query_yes_no("Are sure to delete repositoy '"+repo_name+"'?")):
					browser = get_webdriver({'image':'no','cache':'yes','UI':'yes'})
					delete_repository(browser,repo_name)
				else:
					print("exiting")
			else:
				print(repo_name+": no valid option")
	else:
		print("No argument")

if __name__ == "__main__":
	#command_line()
	github()
