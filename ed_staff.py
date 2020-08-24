import requests
import csv
import time
from bs4 import BeautifulSoup as soup

staff_links = [
	'http://www.inf.ed.ac.uk/people/staff/Ibrahim_Abu_Farha.html',
	'http://www.inf.ed.ac.uk/people/staff/Alham_Fikri_Aji.html',
	'http://www.inf.ed.ac.uk/people/staff/Youssef_Al_Hariri.html',
	'http://www.inf.ed.ac.uk/people/staff/Abeer_Aldayel.html',
	'http://www.inf.ed.ac.uk/people/staff/Beatrice_Alex.html',
	'http://www.inf.ed.ac.uk/people/staff/Stefanos_Angelidis.html',
	'http://www.inf.ed.ac.uk/people/staff/Daniel_Angelov.html',
	'http://www.inf.ed.ac.uk/people/staff/Sima_Bahrani.html',
	'http://www.inf.ed.ac.uk/people/staff/Andrew_Bates.html',
	'http://www.inf.ed.ac.uk/people/staff/Rachel_Bawden.html',
	'http://www.inf.ed.ac.uk/people/staff/Alexandra_Birch-Mayne.html',
	'http://www.inf.ed.ac.uk/people/staff/Mriganka_Biswas.html',
	'http://www.inf.ed.ac.uk/people/staff/Nikolay_Bogoychev.html',
	'http://www.inf.ed.ac.uk/people/staff/Svitlana_Braichenko.html',
	'http://www.inf.ed.ac.uk/people/staff/Michael_Burke.html',
	'http://www.inf.ed.ac.uk/people/staff/Michael_Camilleri.html',
	'http://www.inf.ed.ac.uk/people/staff/Brian_Campbell.html',
	'http://www.inf.ed.ac.uk/people/staff/Andrea_Carmantini.html',
	'http://www.inf.ed.ac.uk/people/staff/Lipeng_Chen.html',
	'http://www.inf.ed.ac.uk/people/staff/Xiao_Chen.html',
	'http://www.inf.ed.ac.uk/people/staff/Carolin_Chermaz.html',
	'http://www.inf.ed.ac.uk/people/staff/Floyd_Chitalu.html',
	'http://www.inf.ed.ac.uk/people/staff/Michele_Ciampi.html',
	'http://www.inf.ed.ac.uk/people/staff/Marco_Console.html',
	'http://www.inf.ed.ac.uk/people/staff/Carmen_Constantin.html',
	'http://www.inf.ed.ac.uk/people/staff/Robert_Court.html',
	'http://www.inf.ed.ac.uk/people/staff/Sara_Dalzel-Job.html',
	'http://www.inf.ed.ac.uk/people/staff/Mahshid_Delavar.html',
	'http://www.inf.ed.ac.uk/people/staff/Radina_Dobreva.html',
	'http://www.inf.ed.ac.uk/people/staff/Aciel_Eshky.html',
	'http://www.inf.ed.ac.uk/people/staff/Yizhou_Fan.html',
	'http://www.inf.ed.ac.uk/people/staff/Elaine_Farrow.html',
	'http://www.inf.ed.ac.uk/people/staff/Simon_Fowler.html',
	'http://www.inf.ed.ac.uk/people/staff/Robert_Furber.html',
	'http://www.inf.ed.ac.uk/people/staff/Vashti_Galpin.html',
	'http://www.inf.ed.ac.uk/people/staff/Teodora-Maria_Georgescu.html',
	'http://www.inf.ed.ac.uk/people/staff/Ulrich_Germann.html',
	'http://www.inf.ed.ac.uk/people/staff/Daniel_Gordon.html',
	'http://www.inf.ed.ac.uk/people/staff/Henry_Gouk.html',
	'http://www.inf.ed.ac.uk/people/staff/Roman_Goulard.html',
	'http://www.inf.ed.ac.uk/people/staff/Avashna_Govender.html',
	'http://www.inf.ed.ac.uk/people/staff/Andreas_Grivas.html',
	'http://www.inf.ed.ac.uk/people/staff/Claire_Grover.html',
	'http://www.inf.ed.ac.uk/people/staff/Roman_Grundkiewicz.html',
	'http://www.inf.ed.ac.uk/people/staff/Liane_Guillou.html',
	'http://www.inf.ed.ac.uk/people/staff/Barry_Haddow.html',
	'http://www.inf.ed.ac.uk/people/staff/Josiah_Hanna.html',
	'http://www.inf.ed.ac.uk/people/staff/Jindrich_Helcl.html',
	'http://www.inf.ed.ac.uk/people/staff/Matthias_Hofer.html',
	'http://www.inf.ed.ac.uk/people/staff/Yordan_Hristov.html',
	'http://www.inf.ed.ac.uk/people/staff/Craig_Innes.html',
	'http://www.inf.ed.ac.uk/people/staff/Vladimir_Ivan.html',
	'http://www.inf.ed.ac.uk/people/staff/Hua_Ji.html',
	'http://www.inf.ed.ac.uk/people/staff/Ohad_Kammar.html',
	'http://www.inf.ed.ac.uk/people/staff/Theodoros_Kapourniotis.html',
	'http://www.inf.ed.ac.uk/people/staff/Vasileios_Karaiskos.html',
	'http://www.inf.ed.ac.uk/people/staff/Rafael_-_Michael_Karampatsis.html',
	'http://www.inf.ed.ac.uk/people/staff/Jakub_Kaszyk.html',
	'http://www.inf.ed.ac.uk/people/staff/Aydin_Kheirbakhsh_Abadi.html',
	'http://www.inf.ed.ac.uk/people/staff/Jonathan_Kilgour.html',
	'http://www.inf.ed.ac.uk/people/staff/Sanghyun_Kim.html',
	'http://www.inf.ed.ac.uk/people/staff/Ondrej_Klejch.html',
	'http://www.inf.ed.ac.uk/people/staff/Kerewin_Kokke.html',
	'http://www.inf.ed.ac.uk/people/staff/Nina_Kudryashova.html',
	'http://www.inf.ed.ac.uk/people/staff/Niraj_Kumar.html',
	'http://www.inf.ed.ac.uk/people/staff/Benedicte_Legastelois.html',
	'http://www.inf.ed.ac.uk/people/staff/Amelie_Levray.html',
	'http://www.inf.ed.ac.uk/people/staff/Lu_Li.html',
	'http://www.inf.ed.ac.uk/people/staff/Shuo_Li.html',
	'http://www.inf.ed.ac.uk/people/staff/Xueli_Liu.html',
	'http://www.inf.ed.ac.uk/people/staff/Shun_Long.html',
	'http://www.inf.ed.ac.uk/people/staff/Erfan_Loweimi.html',
	'http://www.inf.ed.ac.uk/people/staff/Kevin_Sebastian_Luck.html',
	'http://www.inf.ed.ac.uk/people/staff/Catherine_Magill.html',
	'http://www.inf.ed.ac.uk/people/staff/Carlos_Mastalli_Cadenas.html',
	'http://www.inf.ed.ac.uk/people/staff/Yevgen_Matusevych.html',
	'http://www.inf.ed.ac.uk/people/staff/Colin_McLean.html',
	'http://www.inf.ed.ac.uk/people/staff/Rawad_Mezher.html',
	'http://www.inf.ed.ac.uk/people/staff/Antonio_Miceli_Barone.html',
	'http://www.inf.ed.ac.uk/people/staff/Yumnah_Mohamied.html',
	'http://www.inf.ed.ac.uk/people/staff/John_Morton.html',
	'http://www.inf.ed.ac.uk/people/staff/Uchenna_Nnabuko.html',
	'http://www.inf.ed.ac.uk/people/staff/Kwabena_Nuamah.html',
	'http://www.inf.ed.ac.uk/people/staff/Mateo_Obregon.html',
	'http://www.inf.ed.ac.uk/people/staff/Gideon_Ogunniye.html',
	'http://www.inf.ed.ac.uk/people/staff/Silviu-Vlad_Oprea.html',
	'http://www.inf.ed.ac.uk/people/staff/Kunkun_Pang.html',
	'http://www.inf.ed.ac.uk/people/staff/Massimiliano_Patacchiola.html',
	'http://www.inf.ed.ac.uk/people/staff/Laura_Perez.html',
	'http://www.inf.ed.ac.uk/people/staff/Zoe_Petard.html',
	'http://www.inf.ed.ac.uk/people/staff/Liat_Peterfreund.html',
	'http://www.inf.ed.ac.uk/people/staff/Eugene_Philalithis.html',
	'http://www.inf.ed.ac.uk/people/staff/Paul_Piho.html',
	'http://www.inf.ed.ac.uk/people/staff/Gabriella_Pizzuto.html',
	'http://www.inf.ed.ac.uk/people/staff/Lena_Podoletz.html',
	'http://www.inf.ed.ac.uk/people/staff/Joao_Pousa_De_Moura.html',
	'http://www.inf.ed.ac.uk/people/staff/Martin_Pullinger.html',
	'http://www.inf.ed.ac.uk/people/staff/Christian_Rauch.html',
	'http://www.inf.ed.ac.uk/people/staff/Manuel_Ribeiro.html',
	'http://www.inf.ed.ac.uk/people/staff/Wilmer_Ricciotti.html',
	'http://www.inf.ed.ac.uk/people/staff/Korin_Richmond.html',
	'http://www.inf.ed.ac.uk/people/staff/Quentin_Rouxel.html',
	'http://www.inf.ed.ac.uk/people/staff/Philip_Saville.html',
	'http://www.inf.ed.ac.uk/people/staff/James_Scott-Brown.html',
	'http://www.inf.ed.ac.uk/people/staff/Volker_Seeker.html',
	'http://www.inf.ed.ac.uk/people/staff/Sukanta_Sen.html',
	'http://www.inf.ed.ac.uk/people/staff/Yapeng_Shi.html',
	'http://www.inf.ed.ac.uk/people/staff/Minas_Sifakis.html',
	'http://www.inf.ed.ac.uk/people/staff/Janno_Siim.html',
	'http://www.inf.ed.ac.uk/people/staff/Simon_Smith_Bize.html',
	'http://www.inf.ed.ac.uk/people/staff/Oksana_Sorokina.html',
	'http://www.inf.ed.ac.uk/people/staff/Thomas_Spink.html',
	'http://www.inf.ed.ac.uk/people/staff/Milos_Stanojevic.html',
	'http://www.inf.ed.ac.uk/people/staff/Jan_Stolarek.html',
	'http://www.inf.ed.ac.uk/people/staff/Jiawen_Sun.html',
	'http://www.inf.ed.ac.uk/people/staff/Carlo_Tiseo.html',
	'http://www.inf.ed.ac.uk/people/staff/Richard_Tobin.html',
	'http://www.inf.ed.ac.uk/people/staff/Yi-Shan_Tsai.html',
	'http://www.inf.ed.ac.uk/people/staff/Ioannis_Tselekounis.html',
	'http://www.inf.ed.ac.uk/people/staff/Cassia_Valentini_Botinhao.html',
	'http://www.inf.ed.ac.uk/people/staff/Jelmer_Van_der_Linde.html',
	'http://www.inf.ed.ac.uk/people/staff/Christos_Vasiladiotis.html',
	'http://www.inf.ed.ac.uk/people/staff/Eirini_Vlassi_Pandi.html',
	'http://www.inf.ed.ac.uk/people/staff/William_Waites.html',
	'http://www.inf.ed.ac.uk/people/staff/Chaojun_Wang.html',
	'http://www.inf.ed.ac.uk/people/staff/Lynda_Webb.html',
	'http://www.inf.ed.ac.uk/people/staff/Andrea_Weisse.html',
	'http://www.inf.ed.ac.uk/people/staff/Mirjam_Wester.html',
	'http://www.inf.ed.ac.uk/people/staff/Evelyn_Williams.html',
	'http://www.inf.ed.ac.uk/people/staff/Philip_Williams.html',
	'http://www.inf.ed.ac.uk/people/staff/Steven_Wilson.html',
	'http://www.inf.ed.ac.uk/people/staff/Guiyang_Xin.html',
	'http://www.inf.ed.ac.uk/people/staff/Songyan_Xin.html',
	'http://www.inf.ed.ac.uk/people/staff/Junichi_Yamagishi.html',
	'http://www.inf.ed.ac.uk/people/staff/Lei_Yan.html',
	'http://www.inf.ed.ac.uk/people/staff/Thomas_Zacharias.html',
	'http://www.inf.ed.ac.uk/people/staff/Chenyang_Zhao.html',
	'http://www.inf.ed.ac.uk/people/staff/Rui_Zhao.html'
]

staff_list = {
	'staff':[]
}

for staff in staff_links:
	name = ''
	position = ''
	role = ''
	page = requests.get(url='http://www.inf.ed.ac.uk/people/staff/Ibrahim_Abu_Farha.html')
	raw_html = soup(page.content, 'html.parser')
	name = raw_html.find('b').contents[0]
	info = raw_html.find_all('dd')
	position = info[0].contents[0]
	if 'Member of' in info[1].contents[0]:
		role = info[1].contents[1].contents[0]
	staff_list['staff'].append({
			'name': name,
			'position': position,
			'role': role
		})
	time.sleep(0.2)
save(staff_list)

def save(staff_list):
	with open('staff.csv', 'w', newline='') as f:
		field_name = ['name', 'position', 'role']
		writer = csv.DictWriter(f, fieldnames=field_name)
		writer.writeheader()
		for staff in staff_list['staff']:
			writer.writerow({
					'name': name,
					'position': position,
					'role': role
				})
