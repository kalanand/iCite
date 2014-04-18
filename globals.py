#! /usr/bin/python

## Copyright 2014 Kalanand Mishra

## iCite is a free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 3 of the
## License or any later version: <http://www.gnu.org/licenses/>.
## This software is distributed WITHOUT ANY WARRANTY. 

## Instructions: The main executable is 'analyzer.py'. You can 
## modify input definitions in 'globals.py' according to your needs.
## You can either run a brand-new query (which is the default) or 
## analyze data stored in a text file from a previous query. 

groups = {
    'colliders':  'Collider experiments', 
    'hflavors':   'Flavor physics experiments', 
    'neutrinos':  'Neutrino experiments', 
    'directdm':   'Dark matter experiments', 
    'telescopes': 'Telescopes', 
    'darkenergy': 'Dark energy experiments', 
    'tools':      'HEP tools', 
    'simulation': 'MC simulation',
    'PAGs'      : 'CMS Physics groups'
}


colliders = { ## High energy colliders ##
    "ATLAS": 'collaboration:\'ATLAS\'',
    "CDF":   'collaboration:\'CDF\'',
    "CMS":   'collaboration:\'CMS\'',
    "D0":    'collaboration:\'D0\'',
    "LEP":   'collaboration:\'DELPHI\'+or+collaboration:\'ALEPH\'+or+collaboration:\'L3\'+or+collaboration:\'OPAL\''
}

hflavors = { ## Flavor physics ##
    "LHCB":  'collaboration:\'LHCB\'',
    "BaBar": 'collaboration:\'BABAR\'',
    "Belle": 'collaboration:\'BELLE\'',
    "CLEO":  'collaboration:\'CLEO\'',
    "BES":   'collaboration:\'BES\''
}

neutrinos = { ## Neutrinos ##
    "MINOS":      'collaboration:\'MINOS\'',
    "T2K":        'collaboration:\'T2K\'',
    "DayaBay":    'collaboration:\'DAYA\'',
    "MIN*vA":    'collaboration:\'MINERVA\'',
    "RENO":       'collaboration:\'RENO\'',
    "NOvA":       'collaboration:\'NOVA\'',
    "Ice/PINGU":  'collaboration:\'IceCube\'+or+collaboration:\'PINGU\'',
    "*BooNE":     'collaboration:\'MiniIBooNE\'+or+collaboration:\'MicroBooNE\'+or+collaboration:\'SciBooNE\'',
    "Super-K":    'collaboration:\'Kamiokande\'+or+collaboration:\'Super-Kamiokande\'+or+collaboration:\'Hyper-Kamiokande\''
    ##"LBNE":                          'collaboration:\'LBNE\''
 }

heavyions = { ## Heavy ion ##
    "ALICE":  'collaboration:\'ALICE\'',
    "STAR":   'collaboration:\'STAR\'',
    "PHENIX": 'collaboration:\'PHENIX\'',
    "PHOBOS": 'collaboration:\'PHOBOS\'',
    "BRAHMS": 'collaboration:\'BRAHMS\''
}


directdm = { ## Direct dark matter detection ##
    "LUX":     'collaboration:\'LUX\'',
    "CDMS":    'collaboration:\'CDMS\'',
    "CoGeNT":  'collaboration:\'CoGeNT\'',
    "XENON":   'collaboration:\'XENON\''
}


telescopes = { ## Telescopes, Gamma ray bursts, pulsers ##
    "HAWC/M*gro":   'collaboration:\'HAWC\'+or+collaboration:\'MILAGRO\'',
    "H.E.S.S":        'collaboration:\'H.E.S.S\'',
    "Fermi-LAT":      'collaboration:\'Fermi-LAT\'',
    "VERITAS":        'collaboration:\'VERITAS\'',
    "MAGIC":          'collaboration:\'MAGIC\''
}    


darkenergy = { ## Dark energy ##
    ##"LSST":     'collaboration:\'LSST\'',
    "BOSS":     'collaboration:\'BOSS\'',
    "SDSS":     'collaboration:\'SDSS\'',
    "DES":      'collaboration:\'Dark Energy Survey\'',
    "WMAP":     'collaboration:\'WMAP\'',
    "Planck":   'collaboration:\'Planck\''
}



tools = { ## Tools ##
    "GEANT":    'collaboration:\'GEANT\'',
    "PDG":      'collaboration:\'Particle Data Group\'',
    "CTEQ":     'r+cteq',
    "MSTW":     'a+Thorne+and+a+Martin+and+a+Stirling+and+a+Watt',
    "NNPDF":    'collaboration:\'NNPDF\'',
    "FastJet":  'a+Cacciari+and+a+Salam+and+a+Soyez'
}



simulation = { ## Simulation##
    "Pythia":   'FERMILAB-PUB-07-512-CD-T+or+FERMILAB-PUB-06-052-CD-T+or+FERMILAB-PUB-03-457',
    "BlackHat": 'a+Z.Bern.1+and+a+L.J.Dixon.1+and+a+D.Maitre.1',
    "MCFM":     'a+J.M.Campbell.1+and+a+R.K.Ellis.1',
    "Sherpa":   'a+Krauss+and+a+Schonherr',
    "POWHEG":   'a+P.Nason.1+and+t+powheg',
    "MadGraph": 't+madgraph+or+t+madevent'
}


PAGs = { ## CMS Physics groups ##
    "Std Mod": 'collaboration:\'CMS\'+and+(r+SMP+or+r+EWK+or+eprint+arxiv:1204.3170+or+eprint+arxiv:1311.6141+or+eprint+arxiv:1304.7498+or+eprint+arxiv:1212.6660+or+eprint+arxiv:1110.6461+or+eprint+arxiv:1108.2044+or+eprint+arxiv:1106.0647+or+eprint+arxiv:1106.0208+or+eprint+arxiv:1104.1693+or+eprint+arxiv:1102.2020+or+eprint+arxiv:1102.0068+or+eprint+arxiv:1101.5029)',
    "Higgs":   'collaboration:\'CMS\'+and+r+HIG',
    "Exotics":  'collaboration:\'CMS\'+and+(r+EXO+or+r+B2G)',
    "SUSY":   'collaboration:\'CMS\'+and+r+SUS',
    "Forwd phys":   'collaboration:\'CMS\'+and+(r+FSQ+or+r+FWD+or+eprint+arXiv:1305.6016+or+eprint+arXiv:1204.1411+or+eprint+arXiv:1104.3547+or+eprint+arXiv:1009.4122+or+eprint+arXiv:1102.0068+or+eprint+arXiv:1107.0330+or+eprint+arXiv:1102.4282+or+eprint+arXiv:1011.5531+or+eprint+arXiv:1006.2083+or+eprint+arXiv:1005.3299+or+eprint+arXiv:1101.3518+or+eprint+arXiv:1005.3294+or+eprint+arXiv:1002.0621)', 
    "Top":   'collaboration:\'CMS\'+and+r+TOP',
    "Flavor phys":   'collaboration:\'CMS\'+and+r+BPH',
    "Heavy ion":   'collaboration:\'CMS\'+and+r+HIN', 
    "Phys obj":'collaboration:\'CMS\'+and+(r+JME+or+r+EGM+or+r+BTV+or+r+TRK+or+r+MUO+or+r+PFT+or+r+LUM)' 
}



