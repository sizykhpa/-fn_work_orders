class Request_data:    
    def __init__(self):
        self.orders_on_page = '200' 
        self.cookie = 'FNSESS=MTo3Njc3MTk6MTo6YzNiYWY3ODUxMjVjYWQ3Zjg1NmJmNzZhOWI3NmMxMWQzYjBkNGZjYzoxNjMzMDE2OTQyOjk3M2JjODQxNTMzMzNiYmE5NTFlZmQzYTM3YjExZGMw'
        self.get_all_work_orders_headers = {'Host': 'api-new.fieldnation.com',
                                            'Accept': '*/*',
                                            'Connection': 'keep-alive',
                                            'x-app-platform': 'iOS',
                                            'Cookie': f'{self.cookie}; rememberme=1',
                                            'Accept-Language': 'en-us',
                                            'x-app-version': '21.18.0.63',
                                            'Accept-Encoding': 'gzip, deflate, br',
                                            'User-Agent': 'Field%20Nation/1 CFNetwork/1220.1 Darwin/20.3.0'
                                            }

        self.login_and_refresh_headers = {'Host': 'api-new.fieldnation.com',
                                          'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
                                          'Cookie': f'{self.cookie}; rememberme=1',
                                          'Connection': 'keep-alive',
                                          'Accept': '*/*',
                                          'User-Agent': 'Field Nation/21.18.0 (com.fieldnation.ios; build:1; iOS 14.4.2) Alamofire/21.18.0',
                                          'Accept-Language': 'en-US;q=1.0',
                                          'Accept-Encoding': 'gzip;1=1.0, compress;q=0.5'
                                          }
    
    def login_fn(self, username, password):
        url = 'https://api-new.fieldnation.com/authentication/api/oauth/token?as_provider=1'
        headers = self.login_and_refresh_headers
        body = f'client_id=ios20.26&client_secret=PpCtV%21G%40dmt%2BL%21%25%2AV8SSRs_fNHb%245Qp%24&grant_type=password&password={password}&scope=viewprofile&username={username}'
        return url, headers, body
    
    def refresh_fn(self, refresh_token):
        url =  'https://api-new.fieldnation.com/authentication/api/oauth/refresh?as_provider=1'
        headers = self.login_and_refresh_headers
        body = f'client_id=ios20.26&client_secret=PpCtV%21G%40dmt%2BL%21%25%2AV8SSRs_fNHb%245Qp%24&grant_type=refresh_token&refresh_token={refresh_token}'
        return url, headers, body

    def logout_fn(self, access_token):
        url = f'https://api-new.fieldnation.com/api/rest/v2/profile/remove_device/apns?access_token={access_token}'    
        headers = self.get_all_work_orders_headers
        return url, headers

    def all_work_orders(self, access_token):
        url = f'https://api-new.fieldnation.com/api/rest/v2/workorders?list=workorders_available&columns=id%2Ctitle%2Ctype_of_work%2Ccompany%2Clocation%2Cbundle%2Cpay%2Cschedule%2Cactions%2Ctime_logs%2Cstatus%2Crequests%2Ceta%2Croutes%2Cproblems%2Cholds%2Cdeclines%2Ccontacts%2Cratings%2Cdistance%2Cbuyer_rating%2Ccorrelation_id%2Csmart_matched&page=1&per_page={self.orders_on_page}&view=model&sticky=1&stickyName=mobile&access_token={access_token}'
        headers = self.get_all_work_orders_headers
        return url, headers

# start_time = time.time()
# print("--- %s seconds ---" % (time.time() - start_time))