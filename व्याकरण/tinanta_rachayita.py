from pratyaahaara import expand_pratyahaara
from sutra import *
from vinyaasa import get_shabda, get_vinyaasa
from get_dhaatu import get_dhaatu
import yaml
from pathlib import Path

class Tin:

    def __init__(self, ll):

        self.लकार = ll['लकार']
        self.प्रयोग = ll['प्रयोग']
        self.पुरुष = ll['पुरुष']
        self.वचन = ll['वचन']
        
        if self.प्रयोग == 'कर्तरि':
        	dd = get_dhaatu(ll)
        	assert len(dd) == 1
        	dd = dd[0]
        	print(dd.गण)
        	
        	
if __name__ == '__main__':
	

	query = yaml.safe_load(Path('input.yml').read_text())

	tt = Tin(query)
