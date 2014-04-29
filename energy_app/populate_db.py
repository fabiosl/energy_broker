import random
from energy_app.models import *

def getRandomLocation():
	locations = ["Murmansk,Russia","Arkhangelsk,Russia","Saint Petersburg,Russia","Magadan,Russia","Perm',Russia","Yekaterinburg,Russia","Nizhniy Novgorod,Russia","Glasgow,UK","Kazan',Russia","Chelyabinsk,Russia","Omsk,Russia","Novosibirsk,Russia","Ufa,Russia","Vilnius,Lithuania","Belfast,UK","Gdansk,Poland","Minsk,Byelarus","Leeds,UK","Hamburg,Germany","Manchester,UK","Sheffield,UK","Dublin,Ireland","Samara,Russia","Bremen,Germany","Berlin,Germany","Birmingham,UK","Amsterdam,Netherlands","Irkutsk,Russia","Warsaw,Poland","Rotterdam,Netherlands","Lodz,Poland","Dortmund,Germany","Duisburg,Germany","London,UK","Essen,Germany","Leipzig,Germany","Antwerpen,Belgium","Wroclaw,Poland","Gent,Belgium","Dresden,Germany","Calgary,Canada","Koln,Germany","Bruxelles,Belgium","Bonn,Germany","Lille,France","Liege,Belgium","Kiev,Ukraine","Frankfurt am Main,Germany","Praha,Czech Repub","Krakow,Poland","Winnipeg,Canada","Karaganda,Kazakhstan","Lvov,Ukraine","Brno,Czech Repub","Paris,France","Volgograd,Russia","Strasbourg,France","Linz,Austria","Vienna,Austria","Munchen,Germany","Donets'k,Ukraine","Ulaanbaatar,Mongolia","Budapest,Hungary","Qiqihar,China","Innsbruck,Austria","Rostov-na-Donu,Russia","Nantes,France","Graz,Austria","Bern,Switzerland","Quebec,Canada","Odessa,Ukraine","Harbin,China","Lyon,France","Montreal,Canada","Milano,Italy","Venezia,Italy","Ottawa,Canada","Torino,Italy","Minneapolis,US","Bordeaux,France","Beograd,Serbia","Bucuresti,Romania","Changchung,China","Jilin,China","Urumqi,China","Firenze,Italy","Toronto,Canada","Toulouse,France","Bilbao,Spain","Almaty,Kazakhstan","Rochester,US","Milwaukee,US","Sapporo,Japan","Buffalo,US","Sofiya,Bulgaria","Detroit,US","Boston,US","Fushun,China","Chicago,US","Shenyang,China","T'Bilisi,Georgia","Zaragoza,Spain","Cleveland,US","Tirane,Albania","Anshan,China","Istanbul,Turkey","Salt Lake City,US","Pittsburgh,US","Madrid,Spain","Baku,Azerbaijan","Yerevan,Armenia","Columbus,US","Ankara,Turkey","Philadelphia,US","Beijing,China","Erzurum,Turkey","Samarkand,Uzbekistan","Tangshan,China","Valencia,Spain","Baltimore,US","Cagliari,Italy","Cincinnati,US","Tianjin,China","Pyongyang,Korea D P Rp","Kansas City,US","Washington D.C.,US","St. Louis,US","Sacramento,US","Tabriz,Iran","Shijiazhuang,China","Ashkhabad,Turkmenistan","Taiyuan,China","Seoul,Korea Rep","Sevilla,Spain","Adana,Turkey","Norfolk,US","Tunis,Tunisia","Zibo,China","Jinan,China","Mosul,Iraq","Mashhad,Iran","Aleppo,Syria","Lanzhou,China","Taegu,Korea Rep","Tehran,Iran","Tokyo,Japan","Kawasaki,Japan","Oklahoma City,US","Yokohama,Japan","Charlotte,US","Pusan,Korea Rep","Nagoya,Japan","Memphis,US","Kyoto,Japan","Zhengzhou,China","Homs,Syria","Luoyang,China","Osaka,Japan","Kabul,Afghanistan","Hiroshima,Japan","Xian,China","Fes,Morocco","Atlanta,US","Islamabad,Pakistan","Rawalpindi,Pakistan","Damascus,Syria","Phoenix,US","Baghdad,Iraq","Dallas,US","Esfahan,Iran","Nanjing,China","Amman,Jordan","Amritsar,India","Lahore,Pakistan","Faisalabad,Pakistan","Shanghai,China","Chengdu,China","Wuhan,China","Al Basra,Iraq","Hangzhou,China","Cairo,Egypt","New Orleans,US","Houston,US","Lhasa,China","Chongqing,China","San Antonio,US","Nanchang,China","New Delhi,India","Delhi,India","Changsha,China","Kathmandu,Nepal","Thimbu,Bhutan","Jaipur,India","Lucknow,India","Guiyang,China","Kanpur,India","Fuzhou,China","Miami,US","Monterrey,Mexico","Patna,India","Hyderabad,Pakistan","Benares,India","Doha,Qatar","Kunming,China","Taipei,Taiwan","T`ai-chung,Taiwan","Dhaka,Bangladesh","Guangzhou,China","Ahmadabad,India","Khulna,Bangladesh","Calcutta,India","Tampico,Mexico","Mandalay,Burma","Mecca,Saudi Arabia","Nagpur,India","Hanoi,Vietnam","Haiphong,Vietnam","Merida,Mexico","Guadalajara,Mexico","Bur Sudan,Sudan","Mexico City,Mexico","Puebla de Zaragoza,Mexico","Pune,India","Port-au-Prince,Haiti","San Juan,Puerto Rico","Kingston,Jamaica","Hyderabad,India","Rangoon,Burma","Sanaa,Yemen","Guatemala,Guatemala","Tegucigalpa,Honduras","Bangkok,Thailand","San Salvador,El Salvador","Niamey,Niger","Madras,India","Bangalore,India","Bamako,Mali","Managua,Nicaragua","Phnom Penh,Cambodia","Ho Chi Minh City,Vietnam","Maracaibo,Venezuela","Caracas,Venezuela","Barquisimeto,Venezuela","San Jose,Costa Rica","Madurai,India","Ibadan,Nigeria","Davao,Philippines","Enugu,Nigeria","Medellin,Colombia","Accra,Ghana","Abidjan,Ivory Coast","Bogota,Colombia","Bangui,Cent Af Rep","Yaounde,Cameroon","Medan,Indonesia","Cali,Colombia","Kuala Lumpur,Malaysia","Muqdisho,Somalia","Kisangani,Zaire","Quito,Ecuador","Iquitos,Peru","Fortaleza,Brazil","Brazzaville,Congo","Kananga,Zaire","Dar es Salaam,Tanzania","Bandung,Indonesia","Recife,Brazil","Benguela,Angola","Brasilia,Brazil","Arequipa,Peru","La Paz,Bolivia","Goiania,Brazil","Santa Cruz de La Sierra,Bolivia","Sucre,Bolivia","Belo Horizonte,Brazil","Rio de Janeiro,Brazil","Sao Paulo,Brazil","Santos,Brazil","Gaborone,Botswana","Curitiba,Brazil","Pretoria,South Africa","Maputo,Mozambique","Johannesburg,South Africa","Brisbane,Australia","Durban,South Africa","Porto Alegre,Brazil","Cordoba,Argentina","Santa Fe,Argentina","Mendoza,Argentina","Rosario,Argentina","Santiago,Chile","Port Elizabeth,South Africa","Sydney,Australia","Buenos Aires,Argentina","Canberra,Australia","Auckland,New Zealand","Melbourne,Australia","Bahia Blanca,Argentina","Christchurch,New Zealand","Helsinki,Finland","Sfax,Tunisia","Kobe,Japan","Jerusalem,Israel","Valencia,Venezuela","Guayaquil,Ecuador","San Francisco,US","Edinburgh,UK","Trieste,Italy","Fukuoka,Japan","Kita Kyushu,Japan","N'Djamena,Chad","Tripoli,Libya","Izmir,Turkey","Kinshasa,Zaire","Adelaide,Australia","Jakarta,Indonesia","Semarang,Indonesia","Callao,Peru","Belem,Brazil","Qingdao,China","Vientiane,Laos","Salzburg,Austria","Zagreb,Croatia","Bujumbura,Burundi","Nicosia,Cyprus","Kigali,Rwanda","Ljubljana,Slovenia","Maseru,Lesotho","Luxembourg,Luxembourg","The Hague,Netherlands","Bratislava,Slovakia","Saskatoon,Canada","Regina,Canada","El Paso,US","Jacksonville,US","Moosonee,Canada,","Schefferville,Canada","Goose Bay,Canada,","Porto Velho,Brazil","Cuzco,Peru","Cuiaba,Brazil","Resistencia,Argentina","Tombouctoo,Mali","Maiduguri,Niger","Matadi,Zaire","Huambo,Angola","Kimberley,South Africa","East London,South Africa","Kahemba","Dodoma,Tanzania","Narvik,Norway","Herat,Afghanistan","Druzba,Russia,","Kashi","Chingmei,Taiwan,","Hue,Vietnam","Kuching,Malaysia","Balikpapan,Indonesia","Chatanga,Russia,","Chita,Russia,","Verkhoyvensk,Russia,","Yakutsk,Russia","Okhotsk,Russia,","Nikolayevsk,Russia,","Yuzhno-Sakhalinsk,Russia,","Alice Springs,Australia,","Cairns,Australia","Townsville,Australia","Rockhampton,Australia","Newcastle","Hobart","Dunedin,New Zealand","Victoria,Canada","Porto Novo,Benin","Douala,Cameroon","Vjuag Padang,Indonesia","Ambon,Indonesia","Inch`on,Korea Rep","Dalian,China","Portland,US","Manaus,Brazil","Santarem,Brazil","Invercargill,New Zealand","Mtwara,Tanzania","Toamasina,Madagascar","Bloemfontein,South Africa","Bulawayo,Zimbabwe","Livingstone,Zambia","Al Madinah,Saudi Arabia","Wadi Halfa,Sudan,","Aswan,Egypt","Murzuq,Libya,","Tindouf,Algeria,","Agadez,Niger","El Obeid,Sudan","Mbandaka,Zaire","Whitehorse,Canada","Punte Arenas,Chile","Puerto Montt","Rio Gallegos,Argentina,","Comodoro Rivadavia,Argentina","Suez,Egypt","Alexandria,Egypt","Mocambique,Mozambique,","Bombay,India","Algiers,Algeria","Kharkov,Ukraine","Dnepropetrovsk,Ukraine","Tallinn,Estonia","Uliastay","Santo Domingo,Dominican Rp","Bandar Seri Begawan,Brunei","Banjul,Gambia","Port of Spain,Trinidad","Acapulco,Mexico","Anadyr,Russia,","Angmagssalik,Greenland","Antofagasta,Chile","Aomori,Japan","Banghazi,Libya","Birdum,Australia,","Boa Vista,Brazil,","Chiclayo,Peru","Chimbote,Peru","Churchill,Canada","Cochin,India","Concepcion,Chile","Coquimbo","Darwin,Australia","Djibouti,Djibouti","Fremantle,Australia","George Town,Malaysia","Godhavn,Greenland","Godthab,Greenland","Halifax,Canada","Hammerfest,Norway","Igarka,Russia,","In Salah,Algeria","Inuvik,Canada,","Kigoma","Kotlas","Laayoune,W","Manado,Indonesia","Mangalore,India","Marrakech","Mbabne,Swaziland","Nagasaki,Japan","Natal,Brazil","Nelson,New Zealand","Nome,US","Noril`sk,Russia","Nouadnibou,Mauritania","Novokuznetsk,Russia","Olympia,US","Padang,Indonesia","Palembang","Patrai,Greece","Petropavloski-Kamchatskiy,Russia","Podgorica,Montenegro","Pointe Noire,Congo","Port Gentil,Gabon","Prince Rupert,Canada","Saint John,Canada","Saint Louis,Senegal","Salekhard,Russia,","Samsun,Turkey","Sao Luis,Brazil","Sarajevo,Bosnia/Herz","Scoresbyund,Greenland,","Sept-Iles,Canada","Seward,US","Skopje","Tamanrasset,Algeria,","Thule","Tiksi,Russia,","Toliara,Madagascar","Trujillo","Vishakhapatnam,India","Vorkuta,Russia","Yazd,Iran","Zahedan,Iran","Aden,Yemen","Adis Abeba,Ethiopia","Al Kuwayt,Kuwait","Antananarivo,Madagascar","Ar Riyad,Saudi Arabia","Asmara,Eritrea","Asuncion,Paraguay","Athinai,Greece","Baotou,China","Barcelona,Spain","Barranquilla,Colombia","Beira,Mozambique","Beirut,Lebanon","Belmopan,Belize","Bergen,Norway","Bissau,GuineaBissau","Cape Town,South Africa","Cardiff,UK","Casablanca,Morocco","Cayenne,Fr Guiana","Chittagong,Bangladesh","Colombo,Sri Lanka","Conakry,Guinea","Dakar,Senegal","Denver,US","Dushanfe,Tajikistan","Edmonton,Canada","El-Giza,Egypt","Freetown,Sierra Leone","Frunze,Kyrgyzstan","Genova,Italy","Georgetown,Guyana","Goteborg","Harare,Zimbabwe","Havana,Cuba","Jiddah,Saudi Arabia","Kampala,Uganda","Kano,Nigeria","Kao-Hsiung,Taiwan","Karachi,Pakistan","Khabarovsk,Russia","Khartoum,Sudan","Kishinev","Kobenhavn,Denmark","Lagos,Nigeria","Le Havre,France","Libreville,Gabon","Lilongwe,Malawi","Lima,Peru","Lisboa,Portugal","Liverpool,UK","Lome,Togo","Los Angeles","Luanda","Lumumbashi,Zaire","Lusaka,Zambia","Malabo,Eq Guinea","Manila,Philippines","Marseille,France","Masqat,Oman","Mazatlan,Mexico","Mombasa,Kenya","Monrovia,Liberia","Montevideo,Uruguay","Moskva,Russia","Nairobi,Kenya","Napoli,Italy","New York,US","Newark,US","Nouakchott,Mauritania","Odense,Denmark","Omdurman,Sudan","Oran,Algeria","Oslo,Norway","Ouagadouou,Burkina Faso","Palermo,Italy","Panama,Panama","Paramaribo,Suriname","Perth,Australia","Port Moresby,Papua N Guin","Porto,Portugal","Qandahar,Afghanistan","Quezon City,Philippines","Rabat,Morocco","Reykjavik,Iceland","Riga,Latvia","Roma,Italy","Salvador,Brazil","Shiraz,Iran","Stockholm,Sweden","Surabaja,Indonesia","T`ai-nan,Taiwan","Tampa,US","Tel Aviv-Yafo,Israel","Thessaloniki,Greece","Toshkent,Uzbekistan","Tripoli,Lebanon","Valparaiso,Chile","Vancouver,Canada","Vladivostok,Russia","Walvis Bay,South Africa","Windhoek,Namibia","Wellington,New Zealand","Seattle,US","San Diego,US","Iquique,Chile","Abu Zaby,Untd Arab Em","San Cristobal,Venezuela","Astrakhan","Ghadamis,Libya,","Salto,Uruguay","Yellowknife,Canada","Hilo,US","Honolulu,US","Anchorage,US","Fairbanks,US","Juneau,US","San Jose,US","Chihuaha,Mexico","Veracruz,Mexico","Oaxaca,Mexico","Longyearbyen,Norway,","Hong Kong,UK","Kowloon,UK","Singapore,Singapore"]
	return locations[random.randint(0,len(locations))]

def drop_db():
	CloudProvider.objects.all().delete()
	PowerProducer.objects.all().delete()
	PowerChunk.objects.all().delete()
	Consumer.objects.all().delete()
	Query.objects.all().delete()
	


def _create_google_big_query_providers(scale_factors):
	for scale_factor in scale_factors:
		dataset_size = float( 1024 * scale_factor)
		cloud = CloudProvider(service_name="Google Big Query Dataset: %d scale_factor" % scale_factor, cost_per_processed_gigabyte=0.005, cost_per_uptime=0, dataset_size=dataset_size)
		cloud.save()

def _create_amazon_redshift_providers(scale_factors):
	for scale_factor in scale_factors:
		dataset_size = float( 1024 * scale_factor)
		cloud = CloudProvider(service_name="Amazon Redshift Dataset: %d scale_factor" % scale_factor, cost_per_processed_gigabyte=0, cost_per_uptime=0.215, dataset_size=dataset_size)
		cloud.save()		

def create_cloud_providers():
	scale_factors = [1, 2, 5, 10, 50, 100]
	_create_google_big_query_providers(scale_factors)
	_create_amazon_redshift_providers(scale_factors)


def create_power_producers():
	p1 = PowerProducer(name="Producer 1", location="Marseille")
	p2 = PowerProducer(name="Producer 2", location="Aix en Provence")
	p3 = PowerProducer(name="Producer 3", location="Nimes")
	p4 = PowerProducer(name="Producer 4", location="Marseille")
	p5 = PowerProducer(name="Producer 5", location="Grenoble")
	p6 = PowerProducer(name="Producer 6", location="Paris")
	p7 = PowerProducer(name="Producer 7", location="Strausburgh")
	for p in [p1,p2,p3,p4,p5,p6,p7]: p.save()

def create_power_chunks(number_of_chunks):
	power_producers = PowerProducer.objects.all()
	cloud_providers = CloudProvider.objects.all()
	
	chunks = []
	for i in range(number_of_chunks):
		amount = random.randint(1,500)
		cost_per_kilowatt = random.uniform(0.5, 2.0)
		time_to_produce = random.randint(0,120)
		is_green = bool(random.getrandbits(1))
		producer = power_producers[random.randint(0,(len(power_producers) - 1))]
		provider = cloud_providers[random.randint(0,(len(cloud_providers) - 1))]
		total_cost = cost_per_kilowatt * amount
		chunk = PowerChunk(amount=amount, cost_per_kilowatt=cost_per_kilowatt, time_to_produce=time_to_produce, is_green=is_green, power_producer=producer, cloud_hosting_chunk=provider, total_cost=total_cost)
		chunks.append(chunk)
	PowerChunk.objects.bulk_create(chunks)

def create_consumers():
	consumers = []
	for name in ["Stanton Morley", "Robin Graeme", "Brody Graeme", "Emmerson Nottley", "Leland Burton", "Bray Garthside", "Jadon Notleigh", "Dickenson Peyton", "Deven Luxford", "Braxton Swet", "Thane Yardley", "Calvert Atherton", "Darwin Sagar", "Edwardo Johnson", "Parry Hallewell", "Catcher Buckley", "Simon Hammett", "Haywood Sweet", "Keyon Shelley", "Ward Lea", "Berenice Myerscough", "Sherlie Blakemore", "Patricia Smithe", "Alena Elton", "Karli Clive", "Ebony Foy", "Calista Swet", "Emily Thorp", "Corinne Stevenson", "Laurel Sutton", "Ebony Dryden", "Kimberley Hayhurst", "Golda Abram", "Brook Whitney", "Kelsie Shurman", "Shir Smithy", "Camila Stampes", "Kierra Sweat", "Elyssa Reid", "Tatyana Garrick"]:
		consumer = Consumer(name=name, location=getRandomLocation())
		consumers.append(consumer)
	Consumer.objects.bulk_create(consumers)



def create_consumer_queries():
	consumers = Consumer.objects.all()
	needed_power = random.randint(10,500)
	max_query_cost = random.uniform(0, 2) # in euros
	max_power_cost = needed_power * random.uniform(0.5, 2.0)
	only_green_energy = models.BooleanField(default=False) 
	query_timeout =  random.uniform(0, 2) # in millis
	consumer = consumers[random.randint(0,(len(consumers) - 1))]
	query = Query(needed_power=needed_power, max_query_cost=max_query_cost, max_power_cost=max_power_cost, only_green_energy=only_green_energy, query_timeout=query_timeout, consumer=consumer)
	query.save()


drop_db()
create_cloud_providers()
create_power_producers()
create_power_chunks(10000)
create_consumers()
create_consumer_queries()
