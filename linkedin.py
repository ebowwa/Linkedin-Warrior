class Linkedin:
    def __init__(self):
        # initialize the webdriver and open the LinkedIn login page
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.linkedin.com/login")
        
        # log in using the credentials from the config file
        log("Trying to log in to LinkedIn")
        self.driver.find_element("id","username").send_keys(config.email)
        self.driver.find_element("id","password").send_keys(config.password)
        self.driver.find_element("xpath",'//*[@id="app__container"]/main/div/form/div[3]/button').click()
        
        # wait for the user to verify their phone number via SMS
        log("Please verify your phone number via SMS and press Enter to continue")
        input()
        
    def apply_to_jobs(self):
        # get the list of job URLs from the urlData.txt file
        with open('data/urlData.txt') as f:
            job_urls = f.read().splitlines()
        
        # iterate through each job URL and apply to the job
        for url in job_urls:
            self.driver.get(url)
            log(f"Applying to job at URL: {url}")
            
            # click the "Easy Apply" button if it exists, otherwise move on to the next job
            try:
                self.driver.find_element(By.XPATH, '//button[text()="Easy Apply"]').click()
            except:
                log("Easy Apply button not found, skipping job")
                continue
                
            # wait for the user to complete the application and press Enter to continue
            log("Please complete the application and press Enter to continue")
            input()
