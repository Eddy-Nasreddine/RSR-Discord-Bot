PRE_REQ_1 = ["Guardsman 1st Class", "Sergeant", "Veteran Guardsman", "Staff Sergeant"] # Pre req 2 combined with 1 bkz im lazy
PRE_REQ_2 = ["Veteran Guardsman", "Staff Sergeant"]

class Item:
    def __init__(self, name, prerequisite=None, rank=None, cost=None):
        self.name = name
        self.prerequisite = prerequisite
        self.rank = rank
        self.cost = cost
    
store = {
    'Carbine Equipment': 
        Item(name='Carbine Equipment', cost=75),
        
    'Medum Bags': 
        Item(name='Medum Bags', cost=225),
        
    'Heavy Bags': 
        Item(name='Heavy Bags', prerequisite='Medum Bags', cost=450),
        
    'Light Bags': 
        Item(name='Light Bags', prerequisite='Heavy Bags', rank=PRE_REQ_1, cost=225),
        
    'Augments': 
        Item(name='Augments', prerequisite='Light Bags', rank=PRE_REQ_2, cost=150),
        
    'Webbing Cosmetics': 
        Item('Webbing Cosmetics', cost=35),
        
    'Unlisted Cosmetics': 
        Item('Unlisted Cosmetics', prerequisite='Webbing Cosmetics', cost=75),
        
    'Standard Issue Lasgun Swap': 
        Item('Standard Issue Lasgun Swap', rank=PRE_REQ_1, cost=150),
        
    'Custom Helmet': 
        Item('Custom Helmet', rank=PRE_REQ_1, cost=450),
    
    'Cadian Pattern Helmet Unlock': 
        Item(name='Cadian Pattern Helmet Unlock', cost=75),

    'Agripina Pattern Helmet Unlock': 
        Item(name='Agripina Pattern Helmet Unlock', prerequisite='Cadian Pattern Helmet Unlock', cost=150),

    'Heavy Helmet Unlock': 
        Item(name='Heavy Helmet Unlock', prerequisite='Agripina Pattern Helmet Unlock', cost=150),

    'Unlisted Helmet': 
        Item(name='Unlisted Helmet', prerequisite='Heavy Helmet Unlock', cost=150),

    'Heavy Flak Equipment': 
        Item(name='Heavy Flak Equipment',prerequisite='Unlisted Helmet', rank=PRE_REQ_1, cost=150),

    'Power Maul': 
        Item(name='Power Maul',prerequisite="Power Fist", rank=PRE_REQ_2, cost=150),

    'Power Longsword': 
        Item(name='Power Longsword', rank=PRE_REQ_2, cost=75),

    'Shovel': 
        Item(name='Shovel', cost=35),

    'Chainsword': 
        Item(name='Chainsword', prerequisite='Shovel', cost=75),

    'Chain Dagger': 
        Item(name='Chain Dagger', prerequisite='Chainsword', cost=35),

    'Chain Axe': 
        Item(name='Chain Axe', prerequisite='Chain Dagger', cost=35),
        
    'Unlisted Melee': 
        Item(name='Unlisted Melee',prerequisite="Chain Axe", rank=PRE_REQ_1, cost=150),

    'Eviserator': 
        Item(name='Eviserator', prerequisite='Unlisted Melee', rank=PRE_REQ_1, cost=75),

    'Power Fist': 
        Item(name='Power Fist', prerequisite='Eviserator', rank=PRE_REQ_1, cost=150),
        
    'Power Sword': 
        Item(name='Power Sword', prerequisite="Power Fist", rank=PRE_REQ_2, cost=150),

    'Experimental Weapon Program': 
        Item(name='Experimental Weapon Program', prerequisite='Power Sword', rank=PRE_REQ_2, cost=225),

    'Las-Pistol Unlock': 
        Item(name='Las-Pistol Unlock', cost=75),

    'Master Crafted Las-Pistol': 
        Item(name='Master Crafted Las-Pistol', prerequisite='Las-Pistol Unlock', cost=150),

    'Solid Projectile Training': 
        Item(name='Solid Projectile Training', prerequisite='Master Crafted Las-Pistol', cost=225),
        
    'Mk IVb Lasgun': 
        Item(name='Mk IVb Lasgun',prerequisite='Solid Projectile Training', rank=PRE_REQ_1, cost=75),

    'Bolter Training': 
        Item(name='Bolter Training',prerequisite='Mk IVb Lasgun', rank=PRE_REQ_2, cost=225),

    'Plasma Pistol Training': 
        Item(name='Plasma Pistol Training', prerequisite='Bolter Training', rank=PRE_REQ_2, cost=150),

    'Storm Bolter Training': 
        Item(name='Storm Bolter Training', prerequisite='Plasma Pistol Training', rank=PRE_REQ_2, cost=300),

    'Medium Stubber Unlock': 
        Item(name='Medium Stubber Unlock', cost=150),

    'Heavy Stubber Unlock': 
        Item(name='Heavy Stubber Unlock', prerequisite='Medium Stubber Unlock', cost=225),

    'Heavy Bolter Training': 
        Item(name='Heavy Bolter Training',prerequisite='Heavy Stubber Unlock', rank=PRE_REQ_2, cost=300),
        
    'Bullshark Shotgun': 
        Item(name='Bullshark Shotgun', cost=150),

    'MkIIb Shotgun': 
        Item(name='MkIIb Shotgun', prerequisite='Bullshark Shotgun', cost=225),
        
    'MkIa Plasma Gun Unlock': 
        Item(name='MkIa Plasma Gun Unlock', cost=75),

    'MkIIIa Plasma Gun': 
        Item(name='MkIIIa Plasma Gun', prerequisite='MkIa Plasma Gun Unlock', cost=150),

    'Heavy Flamer Unlock': 
        Item(name='Heavy Flamer Unlock', prerequisite='MkIIIa Plasma Gun', cost=75),

    'MkIIb Grenade Launcher': 
        Item(name='MkIIb Grenade Launcher',prerequisite='Heavy Flamer Unlock', rank=PRE_REQ_1, cost=75),

    'Mk Ia Grenade Launcher': 
        Item(name='Mk Ia Grenade Launcher', prerequisite='MkIIb Grenade Launcher', rank=PRE_REQ_1, cost=150),

    'MkIa Melta Gun': 
        Item(name='MkIa Melta Gun', prerequisite='Mk Ia Grenade Launcher', rank=PRE_REQ_1, cost=225),

    'Mk IIb Melta Gun': 
        Item(name='Mk IIb Melta Gun', prerequisite='MkIa Melta Gun', rank=PRE_REQ_2, cost=300),
        
    'Vorona Pattern': 
        Item(name='Vorona Pattern', cost=225),

    'Accatran Heavy Rocket Launcher': 
        Item(name='Accatran Heavy Rocket Launcher', prerequisite='Vorona Pattern', cost=300),

    'AT Rocket Systems': 
        Item(name='AT Rocket Systems', cost=35),

    'Duel Stubber Systems': 
        Item(name='Duel Stubber Systems', prerequisite='AT Rocket Systems', cost=75),

    'Heavy Bolter System': 
        Item(name='Heavy Bolter System', prerequisite='Duel Stubber Systems', cost=150),

    'Autocannon System': 
        Item(name='Autocannon System', prerequisite='Heavy Bolter System', cost=150),
        
    'Lascannon System': 
        Item(name='Lascannon System', prerequisite='Autocannon System', rank=PRE_REQ_1, cost=375),

    'Light Mortar': 
        Item(name='Light Mortar', cost=75),

    'Assault Mortar': 
        Item(name='Assault Mortar', prerequisite='Light Mortar', cost=150),

    'Siege Mortar': 
        Item(name='Siege Mortar', prerequisite='Assault Mortar', cost=300),
        
    'HB Chimera': 
        Item(name='HB Chimera', cost=75),

    'Autocannon Chimera': 
        Item(name='Autocannon Chimera', prerequisite='HB Chimera', cost=150),

    'Chimedon Pattern': 
        Item(name='Chimedon Pattern', prerequisite='Autocannon Chimera', cost=75),

    'Chimerro Varient': 
        Item(name='Chimerro Varient', prerequisite='Chimedon Pattern', cost=75),
        
    'Basilisk Pattern': 
        Item(name='Basilisk Pattern',prerequisite='Chimerro Varient', rank=PRE_REQ_1, cost=150),

    'Medusa Pattern': 
        Item(name='Medusa Pattern', prerequisite='Basilisk Pattern', rank=PRE_REQ_1, cost=225),
        
    'Hellhound Chimera': 
        Item(name='Hellhound Chimera', prerequisite='Autocannon Chimera', cost=150),

    'DevilDog Chimera': 
        Item(name='DevilDog Chimera', prerequisite='Hellhound Chimera', cost=150),

    'Hydra Pattern': 
        Item(name='Hydra Pattern',prerequisite='DevilDog Chimera', rank=PRE_REQ_1, cost=75),

    'Wyvern Pattern': 
        Item(name='Wyvern Pattern', prerequisite='Hydra Pattern', rank=PRE_REQ_1, cost=150),

    'HB Leman': 
        Item(name='HB Leman', cost=75),

    'Battle Cannon Leman': 
        Item(name='Battle Cannon Leman', prerequisite='HB Leman', cost=150),

    'Punisher Leman': 
        Item(name='Punisher Leman', prerequisite='Battle Cannon Leman', cost=150),

    'Vanquisher Leman': 
        Item(name='Vanquisher Leman', prerequisite='Punisher Leman', cost=225),

    'Executioner Leman': 
        Item(name='Executioner Leman', prerequisite='Battle Cannon Leman', cost=225),

    'Annihilator Leman': 
        Item(name='Annihilator Leman', prerequisite='Executioner Leman', cost=225),
        
    'Conqueror Leman': 
        Item(name='Conqueror Leman', prerequisite='Battle Cannon Leman', cost=150),

    'Demolisher Leman': 
        Item(name='Demolisher Leman', prerequisite='Conqueror Leman', cost=225),

    'Baneblade Pattern': 
        Item(name='Baneblade Pattern', prerequisite=['Annihilator Leman', 'Vanquisher Leman', 'Demolisher Leman'], rank=PRE_REQ_1, cost=600),

    'Tauros HMG': 
        Item(name='Tauros HMG', cost=75),

    'Tauros GMG': 
        Item(name='Tauros GMG', prerequisite='Tauros HMG', cost=75),

    'Tauros Venator': 
        Item(name='Tauros Venator', prerequisite='Tauros GMG', cost=150),
        
    'Taurox Stubber': 
        Item(name='Taurox Stubber', cost=75),

    'Taurox Gatling': 
        Item(name='Taurox Gatling', prerequisite='Taurox Stubber', cost=150),

    'Taurox Autocannon': 
        Item(name='Taurox Autocannon', prerequisite='Taurox Gatling', cost=150),

    'Taurox BattleCannon': 
        Item(name='Taurox BattleCannon', prerequisite='Taurox Autocannon', cost=225),
       
    'Test Item': Item(name='Test Item', cost=100),
}


