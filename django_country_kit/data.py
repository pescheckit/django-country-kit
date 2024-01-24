from django.utils.translation import gettext_lazy as _

COUNTRIES = {
    "AF": {"name": _("Afghanistan"), "alpha3": "AFG"},
    "AX": {"name": _("Åland Islands"), "alpha3": "ALA"},
    "AL": {"name": _("Albania"), "alpha3": "ALB"},
    "DZ": {"name": _("Algeria"), "alpha3": "DZA"},
    "AS": {"name": _("American Samoa"), "alpha3": "ASM"},
    "AD": {"name": _("Andorra"), "alpha3": "AND"},
    "AO": {"name": _("Angola"), "alpha3": "AGO"},
    "AI": {"name": _("Anguilla"), "alpha3": "AIA"},
    "AQ": {"name": _("Antarctica"), "alpha3": "ATA"},
    "AG": {"name": _("Antigua and Barbuda"), "alpha3": "ATG"},
    "AR": {"name": _("Argentina"), "alpha3": "ARG"},
    "AM": {"name": _("Armenia"), "alpha3": "ARM"},
    "AW": {"name": _("Aruba"), "alpha3": "ABW"},
    "AU": {"name": _("Australia"), "alpha3": "AUS"},
    "AT": {"name": _("Austria"), "alpha3": "AUT"},
    "AZ": {"name": _("Azerbaijan"), "alpha3": "AZE"},
    "BS": {"name": _("Bahamas"), "alpha3": "BHS"},
    "BH": {"name": _("Bahrain"), "alpha3": "BHR"},
    "BD": {"name": _("Bangladesh"), "alpha3": "BGD"},
    "BB": {"name": _("Barbados"), "alpha3": "BRB"},
    "BY": {"name": _("Belarus"), "alpha3": "BLR"},
    "BE": {"name": _("Belgium"), "alpha3": "BEL"},
    "BZ": {"name": _("Belize"), "alpha3": "BLZ"},
    "BJ": {"name": _("Benin"), "alpha3": "BEN"},
    "BM": {"name": _("Bermuda"), "alpha3": "BMU"},
    "BT": {"name": _("Bhutan"), "alpha3": "BTN"},
    "BO": {"name": _("Bolivia"), "alpha3": "BOL"},
    "BA": {"name": _("Bosnia and Herzegovina"), "alpha3": "BIH"},
    "BW": {"name": _("Botswana"), "alpha3": "BWA"},
    "BV": {"name": _("Bouvet Island"), "alpha3": "BVT"},
    "BR": {"name": _("Brazil"), "alpha3": "BRA"},
    "IO": {"name": _("British Indian Ocean Territory"), "alpha3": "IOT"},
    "BN": {"name": _("Brunei Darussalam"), "alpha3": "BRN"},
    "BG": {"name": _("Bulgaria"), "alpha3": "BGR"},
    "BF": {"name": _("Burkina Faso"), "alpha3": "BFA"},
    "BI": {"name": _("Burundi"), "alpha3": "BDI"},
    "KH": {"name": _("Cambodia"), "alpha3": "KHM"},
    "CM": {"name": _("Cameroon"), "alpha3": "CMR"},
    "CA": {"name": _("Canada"), "alpha3": "CAN"},
    "CV": {"name": _("Cape Verde"), "alpha3": "CPV"},
    "KY": {"name": _("Cayman Islands"), "alpha3": "CYM"},
    "CF": {"name": _("Central African Republic"), "alpha3": "CAF"},
    "TD": {"name": _("Chad"), "alpha3": "TCD"},
    "CL": {"name": _("Chile"), "alpha3": "CHL"},
    "CN": {"name": _("China"), "alpha3": "CHN"},
    "CX": {"name": _("Christmas Island"), "alpha3": "CXR"},
    "CC": {"name": _("Cocos (Keeling) Islands"), "alpha3": "CCK"},
    "CO": {"name": _("Colombia"), "alpha3": "COL"},
    "KM": {"name": _("Comoros"), "alpha3": "COM"},
    "CG": {"name": _("Congo"), "alpha3": "COG"},
    "CD": {"name": _("Congo, The Democratic Republic of the"), "alpha3": "COD"},
    "CK": {"name": _("Cook Islands"), "alpha3": "COK"},
    "CR": {"name": _("Costa Rica"), "alpha3": "CRI"},
    "CI": {"name": _("Cote D'Ivoire"), "alpha3": "CIV"},
    "HR": {"name": _("Croatia"), "alpha3": "HRV"},
    "CU": {"name": _("Cuba"), "alpha3": "CUB"},
    "CY": {"name": _("Cyprus"), "alpha3": "CYP"},
    "CZ": {"name": _("Czech Republic"), "alpha3": "CZE"},
    "DK": {"name": _("Denmark"), "alpha3": "DNK"},
    "DJ": {"name": _("Djibouti"), "alpha3": "DJI"},
    "DM": {"name": _("Dominica"), "alpha3": "DMA"},
    "DO": {"name": _("Dominican Republic"), "alpha3": "DOM"},
    "EC": {"name": _("Ecuador"), "alpha3": "ECU"},
    "EG": {"name": _("Egypt"), "alpha3": "EGY"},
    "SV": {"name": _("El Salvador"), "alpha3": "SLV"},
    "GQ": {"name": _("Equatorial Guinea"), "alpha3": "GNQ"},
    "ER": {"name": _("Eritrea"), "alpha3": "ERI"},
    "EE": {"name": _("Estonia"), "alpha3": "EST"},
    "ET": {"name": _("Ethiopia"), "alpha3": "ETH"},
    "FK": {"name": _("Falkland Islands (Malvinas)"), "alpha3": "FLK"},
    "FO": {"name": _("Faroe Islands"), "alpha3": "FRO"},
    "FJ": {"name": _("Fiji"), "alpha3": "FJI"},
    "FI": {"name": _("Finland"), "alpha3": "FIN"},
    "FR": {"name": _("France"), "alpha3": "FRA"},
    "GF": {"name": _("French Guiana"), "alpha3": "GUF"},
    "PF": {"name": _("French Polynesia"), "alpha3": "PYF"},
    "TF": {"name": _("French Southern Territories"), "alpha3": "ATF"},
    "GA": {"name": _("Gabon"), "alpha3": "GAB"},
    "GM": {"name": _("Gambia"), "alpha3": "GMB"},
    "GE": {"name": _("Georgia"), "alpha3": "GEO"},
    "DE": {"name": _("Germany"), "alpha3": "DEU"},
    "GH": {"name": _("Ghana"), "alpha3": "GHA"},
    "GI": {"name": _("Gibraltar"), "alpha3": "GIB"},
    "GR": {"name": _("Greece"), "alpha3": "GRC"},
    "GL": {"name": _("Greenland"), "alpha3": "GRL"},
    "GD": {"name": _("Grenada"), "alpha3": "GRD"},
    "GP": {"name": _("Guadeloupe"), "alpha3": "GLP"},
    "GU": {"name": _("Guam"), "alpha3": "GUM"},
    "GT": {"name": _("Guatemala"), "alpha3": "GTM"},
    "GG": {"name": _("Guernsey"), "alpha3": "GGY"},
    "GN": {"name": _("Guinea"), "alpha3": "GIN"},
    "GW": {"name": _("Guinea-Bissau"), "alpha3": "GNB"},
    "GY": {"name": _("Guyana"), "alpha3": "GUY"},
    "HT": {"name": _("Haiti"), "alpha3": "HTI"},
    "HM": {"name": _("Heard Island and Mcdonald Islands"), "alpha3": "HMD"},
    "VA": {"name": _("Holy See (Vatican City State)"), "alpha3": "VAT"},
    "HN": {"name": _("Honduras"), "alpha3": "HND"},
    "HK": {"name": _("Hong Kong"), "alpha3": "HKG"},
    "HU": {"name": _("Hungary"), "alpha3": "HUN"},
    "IS": {"name": _("Iceland"), "alpha3": "ISL"},
    "IN": {"name": _("India"), "alpha3": "IND"},
    "ID": {"name": _("Indonesia"), "alpha3": "IDN"},
    "IR": {"name": _("Iran, Islamic Republic Of"), "alpha3": "IRN"},
    "IQ": {"name": _("Iraq"), "alpha3": "IRQ"},
    "IE": {"name": _("Ireland"), "alpha3": "IRL"},
    "IM": {"name": _("Isle of Man"), "alpha3": "IMN"},
    "IL": {"name": _("Israel"), "alpha3": "ISR"},
    "IT": {"name": _("Italy"), "alpha3": "ITA"},
    "JM": {"name": _("Jamaica"), "alpha3": "JAM"},
    "JP": {"name": _("Japan"), "alpha3": "JPN"},
    "JE": {"name": _("Jersey"), "alpha3": "JEY"},
    "JO": {"name": _("Jordan"), "alpha3": "JOR"},
    "KZ": {"name": _("Kazakhstan"), "alpha3": "KAZ"},
    "KE": {"name": _("Kenya"), "alpha3": "KEN"},
    "KI": {"name": _("Kiribati"), "alpha3": "KIR"},
    "KP": {"name": _("Korea, Democratic People's Republic of"), "alpha3": "PRK"},
    "KR": {"name": _("Korea, Republic of"), "alpha3": "KOR"},
    "KW": {"name": _("Kuwait"), "alpha3": "KWT"},
    "KG": {"name": _("Kyrgyzstan"), "alpha3": "KGZ"},
    "LA": {"name": _("Lao People's Democratic Republic"), "alpha3": "LAO"},
    "LV": {"name": _("Latvia"), "alpha3": "LVA"},
    "LB": {"name": _("Lebanon"), "alpha3": "LBN"},
    "LS": {"name": _("Lesotho"), "alpha3": "LSO"},
    "LR": {"name": _("Liberia"), "alpha3": "LBR"},
    "LY": {"name": _("Libyan Arab Jamahiriya"), "alpha3": "LBY"},
    "LI": {"name": _("Liechtenstein"), "alpha3": "LIE"},
    "LT": {"name": _("Lithuania"), "alpha3": "LTU"},
    "LU": {"name": _("Luxembourg"), "alpha3": "LUX"},
    "MO": {"name": _("Macao"), "alpha3": "MAC"},
    "MK": {"name": _("Macedonia, The Former Yugoslav Republic of"), "alpha3": "MKD"},
    "MG": {"name": _("Madagascar"), "alpha3": "MDG"},
    "MW": {"name": _("Malawi"), "alpha3": "MWI"},
    "MY": {"name": _("Malaysia"), "alpha3": "MYS"},
    "MV": {"name": _("Maldives"), "alpha3": "MDV"},
    "ML": {"name": _("Mali"), "alpha3": "MLI"},
    "MT": {"name": _("Malta"), "alpha3": "MLT"},
    "MH": {"name": _("Marshall Islands"), "alpha3": "MHL"},
    "MQ": {"name": _("Martinique"), "alpha3": "MTQ"},
    "MR": {"name": _("Mauritania"), "alpha3": "MRT"},
    "MU": {"name": _("Mauritius"), "alpha3": "MUS"},
    "YT": {"name": _("Mayotte"), "alpha3": "MYT"},
    "MX": {"name": _("Mexico"), "alpha3": "MEX"},
    "FM": {"name": _("Micronesia, Federated States of"), "alpha3": "FSM"},
    "MD": {"name": _("Moldova, Republic of"), "alpha3": "MDA"},
    "MC": {"name": _("Monaco"), "alpha3": "MCO"},
    "MN": {"name": _("Mongolia"), "alpha3": "MNG"},
    "MS": {"name": _("Montserrat"), "alpha3": "MSR"},
    "MA": {"name": _("Morocco"), "alpha3": "MAR"},
    "MZ": {"name": _("Mozambique"), "alpha3": "MOZ"},
    "MM": {"name": _("Myanmar"), "alpha3": "MMR"},
    "NA": {"name": _("Namibia"), "alpha3": "NAM"},
    "NR": {"name": _("Nauru"), "alpha3": "NRU"},
    "NP": {"name": _("Nepal"), "alpha3": "NPL"},
    "NL": {"name": _("Netherlands"), "alpha3": "NLD"},
    "AN": {"name": _("Netherlands Antilles"), "alpha3": "ANT"},
    "NC": {"name": _("New Caledonia"), "alpha3": "NCL"},
    "NZ": {"name": _("New Zealand"), "alpha3": "NZL"},
    "NI": {"name": _("Nicaragua"), "alpha3": "NIC"},
    "NE": {"name": _("Niger"), "alpha3": "NER"},
    "NG": {"name": _("Nigeria"), "alpha3": "NGA"},
    "NU": {"name": _("Niue"), "alpha3": "NIU"},
    "NF": {"name": _("Norfolk Island"), "alpha3": "NFK"},
    "MP": {"name": _("Northern Mariana Islands"), "alpha3": "MNP"},
    "NO": {"name": _("Norway"), "alpha3": "NOR"},
    "OM": {"name": _("Oman"), "alpha3": "OMN"},
    "PK": {"name": _("Pakistan"), "alpha3": "PAK"},
    "PW": {"name": _("Palau"), "alpha3": "PLW"},
    "PS": {"name": _("Palestinian Territory, Occupied"), "alpha3": "PSE"},
    "PA": {"name": _("Panama"), "alpha3": "PAN"},
    "PG": {"name": _("Papua New Guinea"), "alpha3": "PNG"},
    "PY": {"name": _("Paraguay"), "alpha3": "PRY"},
    "PE": {"name": _("Peru"), "alpha3": "PER"},
    "PH": {"name": _("Philippines"), "alpha3": "PHL"},
    "PN": {"name": _("Pitcairn"), "alpha3": "PCN"},
    "PL": {"name": _("Poland"), "alpha3": "POL"},
    "PT": {"name": _("Portugal"), "alpha3": "PRT"},
    "PR": {"name": _("Puerto Rico"), "alpha3": "PRI"},
    "QA": {"name": _("Qatar"), "alpha3": "QAT"},
    "RE": {"name": _("Reunion"), "alpha3": "REU"},
    "RO": {"name": _("Romania"), "alpha3": "ROU"},
    "RU": {"name": _("Russian Federation"), "alpha3": "RUS"},
    "RW": {"name": _("Rwanda"), "alpha3": "RWA"},
    "SH": {"name": _("Saint Helena"), "alpha3": "SHN"},
    "KN": {"name": _("Saint Kitts and Nevis"), "alpha3": "KNA"},
    "LC": {"name": _("Saint Lucia"), "alpha3": "LCA"},
    "PM": {"name": _("Saint Pierre and Miquelon"), "alpha3": "SPM"},
    "VC": {"name": _("Saint Vincent and the Grenadines"), "alpha3": "VCT"},
    "WS": {"name": _("Samoa"), "alpha3": "WSM"},
    "SM": {"name": _("San Marino"), "alpha3": "SMR"},
    "ST": {"name": _("Sao Tome and Principe"), "alpha3": "STP"},
    "SA": {"name": _("Saudi Arabia"), "alpha3": "SAU"},
    "SN": {"name": _("Senegal"), "alpha3": "SEN"},
    "CS": {"name": _("Serbia and Montenegro"), "alpha3": "SCG"},
    "SC": {"name": _("Seychelles"), "alpha3": "SYC"},
    "SL": {"name": _("Sierra Leone"), "alpha3": "SLE"},
    "SG": {"name": _("Singapore"), "alpha3": "SGP"},
    "SK": {"name": _("Slovakia"), "alpha3": "SVK"},
    "SI": {"name": _("Slovenia"), "alpha3": "SVN"},
    "SB": {"name": _("Solomon Islands"), "alpha3": "SLB"},
    "SO": {"name": _("Somalia"), "alpha3": "SOM"},
    "ZA": {"name": _("South Africa"), "alpha3": "ZAF"},
    "GS": {"name": _("South Georgia and the South Sandwich Islands"), "alpha3": "SGS"},
    "ES": {"name": _("Spain"), "alpha3": "ESP"},
    "LK": {"name": _("Sri Lanka"), "alpha3": "LKA"},
    "SD": {"name": _("Sudan"), "alpha3": "SDN"},
    "SR": {"name": _("Suriname"), "alpha3": "SUR"},
    "SJ": {"name": _("Svalbard and Jan Mayen"), "alpha3": "SJM"},
    "SZ": {"name": _("Swaziland"), "alpha3": "SWZ"},
    "SE": {"name": _("Sweden"), "alpha3": "SWE"},
    "CH": {"name": _("Switzerland"), "alpha3": "CHE"},
    "SY": {"name": _("Syrian Arab Republic"), "alpha3": "SYR"},
    "TW": {"name": _("Taiwan, Province of China"), "alpha3": "TWN"},
    "TJ": {"name": _("Tajikistan"), "alpha3": "TJK"},
    "TZ": {"name": _("Tanzania, United Republic of"), "alpha3": "TZA"},
    "TH": {"name": _("Thailand"), "alpha3": "THA"},
    "TL": {"name": _("Timor-Leste"), "alpha3": "TLS"},
    "TG": {"name": _("Togo"), "alpha3": "TGO"},
    "TK": {"name": _("Tokelau"), "alpha3": "TKL"},
    "TO": {"name": _("Tonga"), "alpha3": "TON"},
    "TT": {"name": _("Trinidad and Tobago"), "alpha3": "TTO"},
    "TN": {"name": _("Tunisia"), "alpha3": "TUN"},
    "TR": {"name": _("Türkiye"), "alpha3": "TUR"},
    "TM": {"name": _("Turkmenistan"), "alpha3": "TKM"},
    "TC": {"name": _("Turks and Caicos Islands"), "alpha3": "TCA"},
    "TV": {"name": _("Tuvalu"), "alpha3": "TUV"},
    "UG": {"name": _("Uganda"), "alpha3": "UGA"},
    "UA": {"name": _("Ukraine"), "alpha3": "UKR"},
    "AE": {"name": _("United Arab Emirates"), "alpha3": "ARE"},
    "GB": {"name": _("United Kingdom"), "alpha3": "GBR"},
    "US": {"name": _("United States"), "alpha3": "USA"},
    "UM": {"name": _("United States Minor Outlying Islands"), "alpha3": "UMI"},
    "UY": {"name": _("Uruguay"), "alpha3": "URY"},
    "UZ": {"name": _("Uzbekistan"), "alpha3": "UZB"},
    "VU": {"name": _("Vanuatu"), "alpha3": "VUT"},
    "VE": {"name": _("Venezuela"), "alpha3": "VEN"},
    "VN": {"name": _("Viet Nam"), "alpha3": "VNM"},
    "VG": {"name": _("Virgin Islands, British"), "alpha3": "VGB"},
    "VI": {"name": _("Virgin Islands, U.S."), "alpha3": "VIR"},
    "WF": {"name": _("Wallis and Futuna"), "alpha3": "WLF"},
    "EH": {"name": _("Western Sahara"), "alpha3": "ESH"},
    "YE": {"name": _("Yemen"), "alpha3": "YEM"},
    "ZM": {"name": _("Zambia"), "alpha3": "ZMB"},
    "ZW": {"name": _("Zimbabwe"), "alpha3": "ZWE"},
}

