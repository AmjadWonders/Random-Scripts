# Done at 1/4/2019 1:36 PM. Now, this serves no purpose lmao.
import requests
from time import sleep

class main:
	def __init__(self):
		self.headers = {
			'Host': 'www.instagram.com',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
			'Accept': '*/*',
			'Accept-Language': 'en-US,en;q=0.5',
			'Accept-Encoding': 'gzip, deflate, br',
			'Referer': 'https://www.instagram.com/accounts/edit/',
			'X-CSRFToken': 'C3cf2Z3LTvsdVABvIADccUOsR2r6NvS2',
			'X-Instagram-AJAX': '1',
			'X-Requested-With': 'XMLHttpRequest',
			'Cookie': 'rur=FRC; mid=XC5sLAAEAAFFjdxXtBiSPJaNTLWB; urlgen="{\"178.80.112.250\": 35819}:1gfMmF:C5gRzwkGOmV_Xzg1Gwr8sgWawlE"; ig_vw=1920; ig_pr=1; ig_vh=978; ig_or=landscape-primary; ig_notifications_dismiss=1514709338435; csrftoken=xmFNy0R8AaPZmFGcPF8Ced2jJxkkQYd0; ds_user_id=9382591389; sessionid=9382591389%3AnykBvrd6Mewa9a%3A12',
			'DNT': '1',
			'Connection': 'keep-alive',
		}
		self.data = {
			'username': 'USERNAME',
		}
		self.session = requests.Session()
		self.session.headers.update(self.headers)


		self.turbo()

	def turbo(self):
		while True:
			print(self.session.post('https://www.instagram.com/accounts/edit/', data=self.data).text)
			sleep(5.1)

if __name__ == "__main__":
	main()
