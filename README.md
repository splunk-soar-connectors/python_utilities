[comment]: # "Auto-generated SOAR connector documentation"
# Python Utilities 

Publisher: Robert Martin  
Connector Version: 1\.0\.2  
Product Vendor: Generic  
Product Name: Python Utilities  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 3\.0\.251  

Implements basic python functions for UI access

### Supported Actions  
[regex function](#action-regex-function) - https\://docs\.python\.org/2/library/re\.html  
[find string](#action-find-string) - Find a substring and return the index  
[split string](#action-split-string) - Use regex to split a string into a list  
[get substring](#action-get-substring) - Returns the substring based on the start, end, step indexes  
[get date](#action-get-date) - Returns the current date and time  

## action: 'regex function'
https\://docs\.python\.org/2/library/re\.html

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**start** |  optional  | Starting position of the search \(Default is 0\) | numeric | 
**end** |  optional  | Ending position of the search \(Default is end of string\) | numeric | 
**pattern** |  required  | Regex pattern | string | 
**source\_string** |  required  | Source string | string | 
**replace** |  optional  | Regex replacement value\. The replacement value is only required for sub and subn actions\. For a single space, use ' '\. For deletion, use '' | string | 
**action** |  required  | Action to take on string | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data | string | 
action\_result\.message | string | 
action\_result\.parameter\.start | string | 
action\_result\.parameter\.end | string | 
action\_result\.parameter\.pattern | string | 
action\_result\.parameter\.source\_string | string | 
action\_result\.parameter\.replace | string | 
action\_result\.parameter\.action | string | 
action\_result\.status | string | 
action\_result\.summary | string |   

## action: 'find string'
Find a substring and return the index

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**search\_string** |  required  | Substring to find in a string | string | 
**source\_string** |  required  | String to search with substring | string | 
**source\_string\_start** |  optional  | Starting index for search \(Default is 0\) | numeric | 
**source\_string\_end** |  optional  | Ending index for search \(Default is string length\) | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data | string | 
action\_result\.message | string | 
action\_result\.parameter\.search\_string | string | 
action\_result\.parameter\.source\_string | string | 
action\_result\.parameter\.source\_string\_start | string | 
action\_result\.parameter\.source\_string\_end | string | 
action\_result\.status | string | 
action\_result\.summary | string | 
action\_result\.data\.\*\.search\_string\_index | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'split string'
Use regex to split a string into a list

Type: **generic**  
Read only: **True**

The separator must be a valid regex\. You may also use any single separator\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**separator** |  required  | Separators to split string | string | 
**source\_string** |  required  | String to split | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data | string | 
action\_result\.message | string | 
action\_result\.parameter\.separator | string | 
action\_result\.parameter\.source\_string | string | 
action\_result\.status | string | 
action\_result\.summary | string | 
action\_result\.data\.\*\.list | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get substring'
Returns the substring based on the start, end, step indexes

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**source\_string\_start** |  optional  | Starting position of the string | numeric | 
**source\_string\_end** |  optional  | Ending position of the string | numeric | 
**source\_string\_step** |  optional  | Step | numeric | 
**source\_string** |  required  | Source string | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.data | string | 
action\_result\.message | string | 
action\_result\.parameter\.source\_string | string | 
action\_result\.parameter\.source\_string\_start | string | 
action\_result\.parameter\.source\_string\_end | string | 
action\_result\.parameter\.source\_string\_step | string | 
action\_result\.status | string | 
action\_result\.summary | string | 
action\_result\.data\.\*\.substring | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get date'
Returns the current date and time

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**format\_string** |  optional  | strftime formatted string to return custom results | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.summary | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.parameter\.format\_string | string | 
action\_result\.data | string | 
action\_result\.data\.\*\.local\_year | numeric | 
action\_result\.data\.\*\.local\_month | numeric | 
action\_result\.data\.\*\.local\_day | numeric | 
action\_result\.data\.\*\.local\_hour | numeric | 
action\_result\.data\.\*\.local\_minute | numeric | 
action\_result\.data\.\*\.local\_second | numeric | 
action\_result\.data\.\*\.local\_weekday | numeric | 
action\_result\.data\.\*\.local\_day\_number | numeric | 
action\_result\.data\.\*\.local\_tz | numeric | 
action\_result\.data\.\*\.local\_iso\_week | numeric | 
action\_result\.data\.\*\.local\_iso\_weekday | numeric | 
action\_result\.data\.\*\.local\_custom | string | 
action\_result\.data\.\*\.utc\_year | numeric | 
action\_result\.data\.\*\.utc\_month | numeric | 
action\_result\.data\.\*\.utc\_day | numeric | 
action\_result\.data\.\*\.utc\_hour | numeric | 
action\_result\.data\.\*\.utc\_minute | numeric | 
action\_result\.data\.\*\.utc\_second | numeric | 
action\_result\.data\.\*\.utc\_weekday | numeric | 
action\_result\.data\.\*\.utc\_day\_number | numeric | 
action\_result\.data\.\*\.utc\_tz | numeric | 
action\_result\.data\.\*\.utc\_iso\_week | numeric | 
action\_result\.data\.\*\.utc\_iso\_weekday | numeric | 
action\_result\.data\.\*\.utc\_custom | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 