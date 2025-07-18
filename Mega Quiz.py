import random
full = ['great himalayan','inderkilla','khirganga','pin valley','col. sherjung','simbalbara',
        'hemis','corbett','gangotri','govind','nanda devi','rajaji','valley of flowers',
        'city forest','salim ali','dachigam','kazinag','kishtwar high altitude'
        ,'kalesar','sultanpur','desert np','keoladeo ghana','mukundra hills','ranthambhore','sariska',
        'betla','dudhwa','khangchendzonga','dibru-saikhowa','kaziranga','manas',
        'nameri','orang','raimona','dihang patkai','mouling','namdhapha','intanki',
        'keibul-lamjao','shiroi','murlen','phawngpui','blue mountain','clouded leapard','bison','rajbari',
        'balphakram','nokrek ridge','bux','gorumara','jaldapara','neora vally','singalila','sunderban',
        'mollem','anshi','bandipur','bannerghatta','kudermukh','nagarahole','rajiv gandhi',
        'anamudi shola','eravikulam','mathikettan shola','pambadum shola','periyar','silent valley',
        'guindy','gulf of mannar','indira gandhi','annamalai','mudumalai','mukurthi']
state_to_parks = {
'himachal' : ['great himalayan','inderkilla','khirganga','pin valley','col. sherjung','simbalbara'],
'ladakh' : ['hemis'],
'uk' : ['corbett','gangotri','govind','nanda devi','rajaji','valley of flowers'],
'jammu' : ['city forest','salim ali','dachigam','kazinag','kishtwar high altitude'],
'haryana' : ['kalesar','sultanpur'],
'rajasthan' : ['desert np','keoladeo ghana','mukundra hills','ranthambhore','sariska'],
'jharkhand': ['betla'],
'up' : ['dudhwa'],
'bihar' : ['valmiki'],
'sikkim' : ['khangchendzonga'],
'assam' : ['dibru-saikhowa','kaziranga','manas','nameri','orang','raimona','dihang patkai'],
'arunachal' : ['mouling','namdhapha'],
'nagaland' : ['intanki'],
'manipur' : ['keibul-lamjao','shiroi'],
'mizoram' : ['murlen','phawngpui','blue mountain'],
'tripura' : ['clouded leapard','bison','rajbari'],
'meghalaya' : ['balphakram','nokrek ridge'],
'bengal' : ['bux','gorumara','jaldapara','neora vally','singalila','sunderban'],
'goa' : ['mollem'],
'karnataka' : ['anshi','bandipur','bannerghatta','kudermukh','nagarahole','rajiv gandhi'],
'kerala' : ['anamudi shola','eravikulam','mathikettan shola','pambadum shola','periyar','silent valley'],
'tamil' : ['guindy','gulf of mannar','indira gandhi','annamalai','mudumalai','mukurthi']
}

'''state = [tamil,kerala,karnataka,goa,bengal,meghalaya,tripura,mizoram,manipur,
         nagaland,arunachal,assam,sikkim,up,jharkhand,rajasthan,haryana,jammu,uk,ladakh,himachal]'''

#print(q)
park_to_state = {}
for state, parks in state_to_parks.items():
    for park in parks:
        park_to_state[park] = state
def run():
    score = 0
    chance = 1

    all_parks=list(park_to_state.items())
    question = random.sample(all_parks, 10)
    

    for i, (park_choice, correct_state) in enumerate(question):
        print(f"\nQ{i+1}. Where is {park_choice} National Park?")

        options = [correct_state]
        wrong_states = list(state_to_parks.keys())
        wrong_states.remove(correct_state)
        options += random.sample(wrong_states, 3)
        random.shuffle(options)

        for i, opt in enumerate(options):
            print(f"{chr(65+i)}. {opt.upper()}")
        
        answer = input("Enter the correct answer (A/B/C/D or state name): ").strip().upper()

        correct_option = chr(65 + options.index(correct_state))

        if answer == correct_option or answer == correct_state.upper():
            score += 1
            print("Correct\n")
        elif answer.lower() == "quit":
            quit()
        else:
            print(f"Incorrect. The correct answer is {correct_state.upper()}\n")
    return score

quiz = run()
print(f"\nYour final score is: {quiz}/10")