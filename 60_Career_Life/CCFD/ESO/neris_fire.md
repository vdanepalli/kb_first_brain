you work for a fire department. your department uses eso suite as records management software. In the software, you have a module, fire neris incidents. 
for each incident, you would have to fill and complete an incident report. A single incident report  contains multiple reports as follows. 
I want you to create a flow chart or any chart showing all the tabs, fields, required or not, if they are text/number/select dropdowns etc. 

## Report Tab: Core


Incident onsert date - required 
Incident onset time - required
Incident number - required
Primary incident type - required - select 1
Additional incident type(s) - select upto 2 
Special incident modifiers(s) - select n
Actions taken - select n
No action taken reason - select 1 of (cancelled | no incident found | staged/standby) -- greyed out if Actions taken contains atleast 1 value
Dispatch run number
Initial dispatch code
Was the call an automatic alarm? Yes | No


Was the fire department aid given or received? Yes|No
If Yes, can add n agencies. For each. 
    Aid Direction? - required - Given | Received
    Aid Type - required - Acting as another entity | in lieu of primary entity | in support of primary entity
    Aid department - required - select 1


Non FD Aid Type - select n 

Battalion - select 1
Division - select 1
Station - select 1
Shift - select 1
District - select 1
Zone - select 1
Report writer - select 1
Quality control - select 1


## Report Tab: Narrative 

Describe the final outcomes of the incident - upto 100k chars
Describe any obstacles that impacted the incident - upto 100k chars

## Report Tab: Location

Address
    Number | Distance Marker
    Prefix - select 1 - N, E, W, S, NE, NW, SE, SW
    Street pre-type - select 1 
    Street name
    Street post-type - select 1
    Suffix - select 1
    Directional - select 1 - Southbound, Eastbound, Westbound, Northbound
    Additional location description

Apt/unit/suite

[Add Cross Street] - can add up to 2. optional

City
State/region - select 1
Postal Code
Postal code extension
County
Country - select 1
Latitude
Longitude

Location use - select 1
Is the location in active use? Yes | No
If No, Vacancy Reason - select 1
If Yes, Is the location being used as intended? Yes | No

Does the location have a secondary use type that impacted the incident response? Yes | No
If Yes, Location Secondary use - select 1



Were any people present? Yes | No
Count of people displaced -- number
If > 0, Cause of displacement - select n



## Report Tab: Incident Times

Dispatch call arrival date and time
Dispatch call answering date and time
Dispatch call creation date and time
Incident command established date and time
Incident sizeup complete date and time
Primary search began date and time
Primary search complete date and time
Water on fire date and time
Fire under control date and time
Fire knocked down date and time
Suppression efforts complete date and time
Extrication date and time
Incident clear date and time


## Report Tab: Resources

This tab has two tabs again -- Units and Personnel. 

under Units tab. I can add n units using Add Unit. And for each unit, 

Unable to dispatch -- Yes, No 
Unit name - required - select 1
Response mode to scene - select 1 - Emergent | Non Emergent

Dispatch Date and Time
Enroute Date and Time
On Scene Date and Time
Cleared Date and Time
Cancelled enroute Date and Time
Staged Date and Time
At patient Date and Time
Agency transfer of care Date and Time
Enroute to hospital Date and Time
Arrived at hospital Date and Time
Facility transfer of care Date and Time
Cleared hospital Date and Time

Using Add Personnel button I can add n personnel to this unit. (select n)


Unit Report Writer - Select 1
Unit narrative - upto 50k chars


under Personnel Tab
I can click on add personnel button to add personnel to the personnel not on unit list. 


## Report Tab: Fire

Suppression appliances - select n 
Water supply - required - select 1
Investigation needed - select 1; If Yes, Investigation Type - Select n

Did this fire take place in structure or outdoor? - Required - Structure | Outdoors

If outdoors:

Outdoor fire cause - required
Acres burned

If Structure fire

Conditions on arrival - required - select 1
Did conditions progress beyond those found on arrival? Yes | No
Damage to structure - required - select 1
Floor of origin - required
Room of origin - required - select 1
Structure fire cause - select 1


## Report Tab: Emerging Hazards

In here, I can add n electrification items, n power generation items. 

For each electrification item. 

Electrification type - required - select 1
Was the battery the source or target? - source | target | unk
Suppression efforts - select n 

For each Power generation item.
Power generation type - required - select 1
Type - selct 1
source or target? - source | target 




Was corrugated stainless steel tubing (CSST) a suspected ignition source? Yes | No

If Yes, 

Was the CSST grounded? - no, unk, yes
Was lightning the suspected cause of ignition? no, unk, yes



## Report Tab: Exposures

I can add n exposures. For each exposure. 

Exposure type -- required -- internal | external 
If external: 
    Exposure Item - required - select 1
    Exposure damage - required - select 1
If internal: 
    Exposure damage - required - select 1


Address
    Number | Distance Marker
    Prefix - select 1 - N, E, W, S, NE, NW, SE, SW
    Street pre-type - select 1 
    Street name
    Street post-type - select 1
    Suffix - select 1
    Directional - select 1 - Southbound, Eastbound, Westbound, Northbound
    Additional location description

Apt/unit/suite

[Add Cross Street] - can add up to 2. optional

City
State/region - select 1
Postal Code
Postal code extension
County
Country - select 1
Latitude
Longitude

Location use - select 1
Is the location in active use? Yes | No
If No, Vacancy Reason - select 1
If Yes, Is the location being used as intended? Yes | No

Does the location have a secondary use type that impacted the incident response? Yes | No
If Yes, Location Secondary use - select 1



Were any people present? Yes | No
Count of people displaced -- number
If > 0, Cause of displacement - select n


## Report Tab: Risk Reduction

Was there at least one smoke alarm present? No, Unk, Yes
If yes:
    Was there at least one working or successfully tested smoke alarm? Yes | No
    Smoke alarm types - required - select n 

Was there at least one fire alarm present? No, Unk, Yes
If yes:
    Fire alarm types - required - select n 

Were there any other alarms present?
If yes:
    Other alarm types - required - select n 


Were there any fire suppression systems present? No, Unk, Yes
If yes:
    Fire suppression type - select 1
    Suppression system coverage - ext unk | full | partial 
You can any number of additional fire suppression systems


Was there at least one cooking fire suppression system present? No, Unk, Yes
If Yes:
    Cooking fire suppression systems - required - select n 


## Report Tab: Rescues / Casualties. 

This has two tabs. Non-firefighter. and Firefighter. 

Under Non-firefighter. 

Count of animals rescued. 

I can add any number of rescue/casualty. For each. 

Rescue type - required - select 1
Casualty type - required - injured fatal | injured nonfatal | uninjured
Birth month/year
Gender - select 1
Race - select 1
When was the need for rescue identified? - select 1
Rescue mode - required - select 1
Rescue actions - select n 
Rescue imediments - select n 
Casualty cause - select 1
 

Under firefighter. I can add any number of persons. For each. 

Rescue type - required - select 1
Casualty type -- required - Injured fatal| Injured nonfatal | Uninjured
Personnel - select 1
Birth month/year 
Gender - select 1
Race - select 1
Rank 
Years of Service
Job Classification - select 1


Was a mayday called for this rescue? Yes | No
If Yes:
    Relative time mayday was called - select 1
    Was an RIT team activated following the mayday declaration? -- Yes | No
Rescue mode - required - select 1
Rescue actions - select n 
Rescue impediments - select n 
Unit - select 1
Duty at time of casualty - select 1
Casualty cause - select 1
Casualty action - select 1
PPE worn whenm casualty occurred - select n 
Was an incident command structure in place when this casualty occurred? - yes | no
Relative time of casualty - select 1


## Report Tab: Attachments. 

I can upload any number of attachments. PDF, DOC, PNG, and JPG files are allowed. Max file size of 5MB.
File name, Description, Date modified,  File Type, Actions. 