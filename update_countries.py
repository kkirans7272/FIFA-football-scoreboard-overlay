# -*- coding: utf-8 -*-
import json
import re

with open('SportsRookie Overlay (Offline).html', 'r', encoding='utf-8') as f:
    content = f.read()

template_match = re.search(r'<script type="__bundler/template">\n"(.+)"\n  </script>', content, re.DOTALL)
if not template_match:
    print("ERROR: Could not find template")
    exit(1)

template_json = template_match.group(1)
try:
    template = json.loads('"' + template_json + '"')
except:
    print("ERROR: Could not parse template as JSON string")
    exit(1)

countries_list = {
    'br': {'n': 'Brazil', 'c': 'BRA', 'col': '#FFD200'},
    'pt': {'n': 'Portugal', 'c': 'POR', 'col': '#DA291C'},
    'ar': {'n': 'Argentina', 'c': 'ARG', 'col': '#75AADB'},
    'fr': {'n': 'France', 'c': 'FRA', 'col': '#1E3A8A'},
    'gb-eng': {'n': 'England', 'c': 'ENG', 'col': '#CF142B'},
    'es': {'n': 'Spain', 'c': 'ESP', 'col': '#C60B1E'},
    'de': {'n': 'Germany', 'c': 'GER', 'col': '#111111'},
    'us': {'n': 'USA', 'c': 'USA', 'col': '#3C3B6E'},
    'nl': {'n': 'Netherlands', 'c': 'NED', 'col': '#FF6200'},
    'it': {'n': 'Italy', 'c': 'ITA', 'col': '#0066A3'},
    'cz': {'n': 'Czechia', 'c': 'CZE', 'col': '#1149AC'},
    'mx': {'n': 'Mexico', 'c': 'MEX', 'col': '#00A651'},
    'kr': {'n': 'Korea Republic', 'c': 'KOR', 'col': '#C60C30'},
    'au': {'n': 'Australia', 'c': 'AUS', 'col': '#FFD100'},
    'jp': {'n': 'Japan', 'c': 'JPN', 'col': '#BC002D'},
    'ca': {'n': 'Canada', 'c': 'CAN', 'col': '#FF0000'},
    'ec': {'n': 'Ecuador', 'c': 'ECU', 'col': '#FFD700'},
    'uy': {'n': 'Uruguay', 'c': 'URU', 'col': '#A0D0E8'},
    'ch': {'n': 'Switzerland', 'c': 'SUI', 'col': '#ED2939'},
    'be': {'n': 'Belgium', 'c': 'BEL', 'col': '#FFC71C'},
    'se': {'n': 'Sweden', 'c': 'SWE', 'col': '#1B4F9E'},
    'no': {'n': 'Norway', 'c': 'NOR', 'col': '#1B3B6F'},
    'dk': {'n': 'Denmark', 'c': 'DEN', 'col': '#C8102E'},
    'co': {'n': 'Colombia', 'c': 'COL', 'col': '#FFD700'},
    'ba': {'n': 'Bosnia and Herzegovina', 'c': 'BIH', 'col': '#002395'},
    'qa': {'n': 'Qatar', 'c': 'QAT', 'col': '#8B1538'},
    'ma': {'n': 'Morocco', 'c': 'MAR', 'col': '#CE1126'},
    'sn': {'n': 'Senegal', 'c': 'SEN', 'col': '#007A5E'},
    'hr': {'n': 'Croatia', 'c': 'CRO', 'col': '#FF0000'},
    'sa': {'n': 'Saudi Arabia', 'c': 'KSA', 'col': '#006C35'},
    'gh': {'n': 'Ghana', 'c': 'GHA', 'col': '#CE1126'},
    'ng': {'n': 'Nigeria', 'c': 'NGR', 'col': '#007A5E'},
    'cm': {'n': 'Cameroon', 'c': 'CMR', 'col': '#007A5E'},
    'sc': {'n': 'Scotland', 'c': 'SCO', 'col': '#003366'},
    'at': {'n': 'Austria', 'c': 'AUT', 'col': '#ED2939'},
    'rs': {'n': 'Serbia', 'c': 'SRB', 'col': '#003366'},
    'tn': {'n': 'Tunisia', 'c': 'TUN', 'col': '#CE1126'},
    'ht': {'n': 'Haiti', 'c': 'HTI', 'col': '#003366'},
    'ci': {'n': 'Ivory Coast', 'c': 'CIV', 'col': '#FF9900'},
    'tr': {'n': 'Turkey', 'c': 'TUR', 'col': '#E30613'},
    'py': {'n': 'Paraguay', 'c': 'PAR', 'col': '#003DA5'},
    'cv': {'n': 'Cape Verde', 'c': 'CPV', 'col': '#007FFF'},
    'dz': {'n': 'Algeria', 'c': 'ALG', 'col': '#007FFF'},
    'ir': {'n': 'Iran', 'c': 'IRI', 'col': '#FFFFFF'},
    'nz': {'n': 'New Zealand', 'c': 'NZL', 'col': '#012169'},
    'eg': {'n': 'Egypt', 'c': 'EGY', 'col': '#CE1126'},
    'iq': {'n': 'Iraq', 'c': 'IRQ', 'col': '#007A5E'},
    'uz': {'n': 'Uzbekistan', 'c': 'UZB', 'col': '#003DA5'},
    'cu': {'n': 'Curaçao', 'c': 'CUR', 'col': '#002395'},
    'pa': {'n': 'Panama', 'c': 'PAN', 'col': '#003DA5'},
    'jo': {'n': 'Jordan', 'c': 'JOR', 'col': '#007A5E'},
    'cd': {'n': 'DR Congo', 'c': 'COD', 'col': '#007A5E'},
}

countries_js_parts = []
for code in sorted(countries_list.keys()):
    data = countries_list[code]
    name = data['n']
    c = data['c']
    col = data['col']
    countries_js_parts.append(code + ':{n:"' + name + '",c:"' + c + '",col:"' + col + '"}')

countries_js = 'var COUNTRIES={' + ','.join(countries_js_parts) + '};'

pattern = r'var COUNTRIES\s*=\s*\{[^}]*\};'

if re.search(pattern, template):
    template = re.sub(pattern, countries_js, template)
    print("Updated COUNTRIES object")
else:
    print("ERROR: Could not find COUNTRIES pattern")
    exit(1)

escaped_template = json.dumps(template)[1:-1]

old_template_section = '<script type="__bundler/template">\n"' + template_json + '"\n  </script>'
new_template_section = '<script type="__bundler/template">\n"' + escaped_template + '"\n  </script>'

if old_template_section in content:
    content = content.replace(old_template_section, new_template_section)
    print("Updated template in HTML file")
else:
    print("ERROR: Could not find template section to replace")
    exit(1)

with open('SportsRookie Overlay (Offline).html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Success! Updated COUNTRIES with " + str(len(countries_list)) + " teams")

