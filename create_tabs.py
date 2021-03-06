import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None

#######################################################################################################################################################################

save_path = "Created_tables/"

calendar_filenames = {	"barcelona_calendar" : "../airbnb/barcelona_calendar.csv",\
			"berlin_calendar" : "../airbnb/berlin_calendar.csv",\
			"madrid_calendar" : "../airbnb/madrid_calendar.csv"}

listings_filenames = {	"barcelona_listings" : "../airbnb/barcelona_listings.csv",\
			"berlin_listings" : "../airbnb/berlin_listings_filtered.csv",\
			"madrid_listings" : "../airbnb/madrid_listings_filtered.csv"}

reviews_filenames = {	"barcelona_reviews" : "../airbnb/barcelona_reviews.csv",\
			"berlin_reviews" : "../airbnb/berlin_reviews.csv",\
			"madrid_reviews" : "../airbnb/madrid_reviews.csv"}

#######################################################################################################################################################################
def load_csvs(dico_files):
	tabs = []
	for file in dico_files:
		print("Loading " + file)
		csv = pd.read_csv(dico_files[file])
		if 'listings' in file:
			csv['city'] = file.split('_')[0]
		print("%d tuples loaded" % csv.shape[0])
		tabs.append(csv)
	return pd.concat(tabs)

#######################################################################################################################################################################
def get_distinct_values(pd_frame, field_name):
	values = []
	for i in pd_frame.index:
		row_list = str(pd_frame.get_value(i, field_name))[1:-1].split(',')
		new_tab = []
		for value in row_list:
			value = value.replace('"','')
			value = value.replace("'",'')
			value = value.lstrip()
			if value not in values and value != '':
				values.append(value)
			if value in values:
				new_tab.append(values.index(value))
		new_tab.sort()
		pd_frame.set_value(i, field_name, new_tab)

	return pd.DataFrame({field_name : values})

#######################################################################################################################################################################
def create_tab_from_indexes(pd_frame, field_name, index_name, value_name, tab_name):
	values = []
	indexes = []
	for i in pd_frame.index:
		list = pd_frame.get_value(i, field_name)
		for x in list:
			indexes.append(i)
			values.append(x)
	new_tab = pd.DataFrame({index_name : indexes, value_name : values}).drop_duplicates()
	new_tab = new_tab.set_index(index_name)
	new_tab.to_csv(save_path + tab_name + '.csv')

#######################################################################################################################################################################
def values_to_index(pd_frame_dict, pd_frame, field_name, dest_field_name):
	dico = pd_frame_dict.set_index(field_name).T.to_dict('list')
	for k, v in dico.items():
		dico[k] = dico[k][0]
	pd_frame[dest_field_name] = pd_frame[dest_field_name].map(dico)

#######################################################################################################################################################################
def clean_description(pd_frame, fields_name):
	for field_name in fields_name:
		for i in pd_frame.index:
			description = str(pd_frame.get_value(i, field_name))
			description = description.replace('\n' , ' ')
			description = description.replace('\r' , ' ')
			description.lstrip()
			pd_frame.set_value(i, field_name, description)

######################################################################################################################################################################
def remove_special_character(pd_frame, field_name, character):
	for i in pd_frame.index:
		description = str(pd_frame.get_value(i, field_name))
		description = description.replace(character, '')
		description.lstrip()
		try:
			description = float(description)
		except ValueError:
			description = ''
		pd_frame.set_value(i, field_name, description)

#######################################################################################################################################################################
"""
print("Loading calendars")
calendars = load_csvs(calendar_filenames)
calendars['cid'] = pd.Series(np.arange(len(calendars)), index = calendars.index)
calendars = calendars.set_index('cid')
remove_special_character(calendars, 'price', '$')
calendars.to_csv(save_path + "calendars.csv")
print("Calendars Loaded \n")
"""
#######################################################################################################################################################################
print("Loading listings")
whole_listings = load_csvs(listings_filenames)

# HOSTS
hosts = whole_listings[['host_id', 'host_url', 'host_name', 'host_since', 'host_about',\
			'host_response_time', 'host_thumbnail_url', 'host_response_rate',\
			'host_picture_url', 'host_neighbourhood', 'host_verifications']].drop_duplicates().set_index('host_id').sort_values(by = ['host_id'])

clean_description(hosts, ['host_about', 'host_url', 'host_name', 'host_thumbnail_url', 'host_picture_url'])
remove_special_character(hosts, 'host_response_rate', '%')
hosts = hosts[~hosts.index.duplicated(keep='first')]

response_time = hosts[['host_response_time']].drop_duplicates().dropna()
response_time['res_id'] = pd.Series(np.arange(len(response_time)), index = response_time.index)
values_to_index(response_time, hosts, 'host_response_time', 'host_response_time')
response_time = response_time.set_index('res_id')

verifications = get_distinct_values(hosts, 'host_verifications')
verifications['vid'] = pd.Series(np.arange(len(verifications)), index = verifications.index)
verifications = verifications.set_index('vid')

create_tab_from_indexes(hosts, 'host_verifications', 'hid', 'vid', 'host_verifications')
hosts = hosts.drop('host_verifications', axis = 1)

# LISTINGS
listings = whole_listings[['id', 'host_id', 'neighbourhood', 'listing_url', 'name', 'longitude', 'latitude','summary', 'space', 'description',\
			'neighborhood_overview', 'notes', 'transit','access', 'interaction', 'house_rules', 'picture_url',\
			'is_business_travel_ready', 'require_guest_profile_picture', 'require_guest_phone_verification',\
			'review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness','review_scores_checkin',\
			'review_scores_communication', 'review_scores_location', 'review_scores_value', 'accommodates',\
			'bathrooms', 'bedrooms', 'beds', 'square_feet', 'price', 'weekly_price', 'monthly_price',\
			'security_deposit', 'cleaning_fee', 'guests_included','extra_people', 'minimum_nights', 'maximum_nights',\
			'property_type', 'room_type', 'bed_type', 'cancellation_policy', 'amenities']].set_index('id').sort_values(by = ['id'])

clean_description(listings, ['summary', 'space', 'description', 'neighborhood_overview', 'notes', 'transit', 'access', 'interaction', 'house_rules',\
				'listing_url', 'picture_url'])
remove_special_character(listings, 'price', '$')
remove_special_character(listings, 'weekly_price', '$')
remove_special_character(listings, 'monthly_price', '$')
remove_special_character(listings, 'security_deposit', '$')
remove_special_character(listings, 'cleaning_fee', '$')
remove_special_character(listings, 'extra_people', '$')

property_type = listings[['property_type']].drop_duplicates().dropna()
property_type['prop_id'] = pd.Series(np.arange(len(property_type)), index = property_type.index)
values_to_index(property_type, listings, 'property_type', 'property_type')
property_type = property_type.set_index('prop_id')

room_type = listings[['room_type']].drop_duplicates().dropna()
room_type['room_id'] = pd.Series(np.arange(len(room_type)), index = room_type.index)
values_to_index(room_type, listings, 'room_type', 'room_type')
room_type = room_type.set_index('room_id')

bed_type = listings[['bed_type']].drop_duplicates().dropna()
bed_type['bed_id'] = pd.Series(np.arange(len(bed_type)), index = bed_type.index)
values_to_index(bed_type, listings, 'bed_type','bed_type')
bed_type = bed_type.set_index('bed_id')

cancellation_policy = listings[['cancellation_policy']].drop_duplicates().dropna()
cancellation_policy['cp_id'] = pd.Series(np.arange(len(cancellation_policy)), index = cancellation_policy.index)
values_to_index(cancellation_policy, listings, 'cancellation_policy', 'cancellation_policy')
cancellation_policy = cancellation_policy.set_index('cp_id')

amenities = get_distinct_values(listings, 'amenities')
amenities['aid'] = pd.Series(np.arange(len(amenities)), index = amenities.index)
amenities = amenities.set_index('aid')

create_tab_from_indexes(listings, 'amenities', 'lid', 'aid', 'listings_amenities')
listings = listings.drop('amenities', axis = 1)


# LOCATION (Neighbourhoods / City / Country)

### WITH CITY ###

neighbourhoods = whole_listings[['neighbourhood', 'city']].drop_duplicates().dropna()
neighbourhoods['n_id'] = pd.Series(np.arange(len(neighbourhoods)), index = neighbourhoods.index)
values_to_index(neighbourhoods[['neighbourhood', 'n_id']], hosts, 'neighbourhood', 'host_neighbourhood')
values_to_index(neighbourhoods[['neighbourhood', 'n_id']], listings, 'neighbourhood', 'neighbourhood')
neighbourhoods = neighbourhoods.set_index('n_id')

city = whole_listings[['city', 'country']].drop_duplicates().dropna()
city['city_id'] = pd.Series(np.arange(len(city)), index = city.index)
values_to_index(city[['city', 'city_id']], neighbourhoods, 'city', 'city')
city = city.set_index('city_id')

country = whole_listings[['country', 'country_code']].drop_duplicates().dropna()
country['country_id'] = pd.Series(np.arange(len(country)), index = country.index)
values_to_index(country[['country', 'country_id']], city, 'country', 'country')
country = country.set_index('country_id')


### WITHOUT CITY ###
"""
neighbourhoods = whole_listings[['neighbourhood']].drop_duplicates().dropna()
neighbourhoods['n_id'] = pd.Series(np.arange(len(neighbourhoods)), index = neighbourhoods.index)
values_to_index(neighbourhoods[['neighbourhood', 'n_id']], hosts, 'neighbourhood', 'host_neighbourhood')
values_to_index(neighbourhoods[['neighbourhood', 'n_id']], listings, 'neighbourhood', 'neighbourhood')
neighbourhoods = neighbourhoods.set_index('n_id')

city = whole_listings[['city', 'country']].drop_duplicates().dropna()
city['city_id'] = pd.Series(np.arange(len(city)), index = city.index)
city = city.set_index('city_id')

country = whole_listings[['country', 'country_code']].drop_duplicates().dropna()
country['country_id'] = pd.Series(np.arange(len(country)), index = country.index)
values_to_index(country[['country', 'country_id']], city, 'country', 'country')
country = country.set_index('country_id')
"""

### CSV HOSTS ###
verifications.to_csv(save_path + "verifications.csv")
response_time.to_csv(save_path + "host_response_time.csv")
hosts.to_csv(save_path + "hosts.csv")

### CSV LoCATIONS ###
neighbourhoods.to_csv(save_path + "neighbourhoods.csv")
city.to_csv(save_path + "city.csv")
country.to_csv(save_path + "country.csv")

### CSV LISTINGS ###
listings.to_csv(save_path + "listings.csv")
property_type.to_csv(save_path + "listings_property_type.csv")
room_type.to_csv(save_path + "listings_room_type.csv")
bed_type.to_csv(save_path + "listings_bed_type.csv")
cancellation_policy.to_csv(save_path + "listings_cancellation_policy.csv")
amenities.to_csv(save_path + "amenities.csv")
print("Listings Loaded \n")

#######################################################################################################################################################################
"""
print("Loading reviews")
reviews = load_csvs(reviews_filenames).set_index('id').sort_values(by = ['id'])
clean_description(reviews, ['comments', 'reviewer_name'])
reviews.to_csv(save_path + "reviews.csv")
print("Reviews Loaded \n")
"""
#######################################################################################################################################################################




