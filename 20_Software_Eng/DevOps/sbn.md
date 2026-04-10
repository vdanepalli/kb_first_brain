# Scriban

Similar to Liquid (used by SHopify) or Jinja (used in Python)

`.sbn`

```xml
<Incident>
  <Type>Fire</Type>
  <ID>{{ incident_id }}</ID>
</Incident>
```

`~` controls the whitespace. Strips out spaces, tabs, newlines from the side of the tag it is placed on. 

```xml
<Status>
  {{ if is_active }}
    Active
  {{ end }}
</Status>

<Status>
  
    Active
  
</Status>
```

```xml
<Status>
  {{~ if is_active ~}}
    Active
  {{~ end ~}}
</Status>

<Status>Active</Status>
```

Variables 

```xml
{{ priority_level = 1 }}
{{ dispatch_code = "10-4" }}

<Priority>{{ priority_level }}</Priority>
```

Conditionals 

```xml
{{ if priority_level == 1 }}
  <Response>Emergency Lights and Sirens</Response>
{{ else if priority_level == 2 }}
  <Response>Standard Routing</Response>
{{ else }}
  <Response>Non-Emergency</Response>
{{ end }}

==, ~=, >, <, >=, <=, &&, ||
```

Arrays and Loops

```xml
{{ units = ["Engine 1", "Ladder 4", "Medic 9"] }}

<DispatchedUnits>
  {{~ for unit in units ~}}
    <Unit>{{ unit }}</Unit>
  {{~ end ~}}
</DispatchedUnits>
```

Dictionaries

```xml
{{ 
  status_codes = {
    "DP": "Dispatched",
    "ER": "En Route",
    "OS": "On Scene",
    "TR": "Transporting"
  } 
}}

<CurrentStatus>{{ status_codes[current_status] }}</CurrentStatus>

<CurrentStatus>En Route</CurrentStatus> 
```

Pipes and Built-in functions

```xml
{{ "hello" | string.upcase }}
{{ unit_name | empty ? "Unknown Unit" : unit_name }}
{{ "123 Main St" | string.replace "St" "Street" }}
{{ date.now | date.to_string "%Y-%m-%d" }}
```

`limit` restrict loop iterations
`offset` skip specified number of items
`reversed` loop backwards

```xml
{{ array = [1, 2, 3, 4, 5, 6] }}
{{ for item in array offset:2 limit:3 reversed }}
  {{ item }}
{{ end }}
```

`for` object properties. Inside any for loop, scriban creates `for` object.
`for.index` current index
`for.rindex` current index from end
`for.first` true if this is the very first iteration
`for.last` true if this is the very last iteration
`for.even` true if current `for.index` is even
`for.odd` true if current `for.index` is odd
`for.length` total number of items the loop will process

```xml
[
  {{ for unit in units }}
    "{{ unit }}"{{ if !for.last }},{{ end }}
  {{ end }}
]
```

While Loop

```xml
{{ i = 0 }}
{{ while i < 5 }}
  Count: {{ i }}
  {{ i = i + 1 }}
{{ end }}
```

`unless` opposite of `if`. runs if the conditions is false. 

```xml
{{ unless unit.is_available }}
  <Warning>Unit is currently out of service.</Warning>
{{ end }}
```

Case

```xml
{{ case incident.type }}
{{ when "FIRE" }}
  <Type>Fire Response</Type>
{{ when "MED" }}
  <Type>Medical Emergency</Type>
{{ when "MVA", "TRAFFIC" }} <Type>Traffic Accident</Type>
{{ else }}
  <Type>Unknown Call Type</Type>
{{ end }}
```

Functions 

```xml
{{ func calculate_priority(level, is_hazmat)
     if is_hazmat
       ret "CRITICAL"
     else if level < 3
       ret "HIGH"
     else
       ret "STANDARD"
     end
   end 
}}

<CalculatedPriority>
  {{ calculate_priority 2 true }}
</CalculatedPriority>
```

Arrays and Objects

```xml
{{ if array.size(dispatched_units) > 0 }}
  <UnitsAssigned>Yes</UnitsAssigned>
  <Total>{{ array.size dispatched_units }}</Total>
{{ end }}
```

```xml
{{ incident_data = { "ID": 101, "Type": "Fire" } }}

{{ if object.has_key incident_data "Address" }}
  <Location>{{ incident_data.Address }}</Location>
{{ else }}
  <Location>NO ADDRESS PROVIDED</Location>
{{ end }}
```

Date Manipulation

`date.add_days` / `months` / `years`
`date.add_hours` / `minutes` / `seconds`

```xml
{{ now = date.now }}

{{ future_date = date.add_days now 14 }}

<ExpirationDate>{{ future_date | date.to_string "%Y-%m-%d" }}</ExpirationDate>
```

Anonymous Arguments - Argument Indexing. `$0` first variable passed, `$1` second variable passed, ...

```xml
{{
    func sayHi
        Hello $0
    end
}}
```

`ISO 8601 Format`: Big to Small. `YYYY-MM-DDThh:mm:ssZ` | `±hh:mm` `Z` is UTC

`ret` returns value

