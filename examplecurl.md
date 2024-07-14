curl -X GET "https://clinicaltrials.gov/api/v2/studies?query.cond=lung+cancer&
query.term=AREA%5BLastUpdatePostDate%5DRANGE%5B2023-01-15%2CMAX%5D&
filter.overallStatus=NOT_YET_RECRUITING%2CRECRUITING&
filter.geo=distance%2839.0035707%2C-77.1013313%2C50mi%29&
filter.ids=NCT04852770%2CNCT01728545%2CNCT02109302&
filter.advanced=AREA%5BStartDate%5D2022&
filter.synonyms=ConditionSearch%3A1651367%2CBasicSearch%3A2013558&
postFilter.overallStatus=NOT_YET_RECRUITING%2CRECRUITING&
postFilter.geo=distance%2839.0035707%2C-77.1013313%2C50mi%29&
postFilter.ids=NCT04852770%2CNCT01728545%2CNCT02109302&
postFilter.advanced=AREA%5BStartDate%5D2022&
postFilter.synonyms=ConditionSearch%3A1651367%2CBasicSearch%3A2013558&
aggFilters=results%3Awith%2Cstatus%3Acom&
geoDecay=func%3Alinear%2Cscale%3A100km%2Coffset%3A10km%2Cdecay%3A0.1&
fields=NCTId%2CBriefTitle%2COverallStatus%2CHasResults&
sort=%40relevance&
pageSize=2" \
 -H "accept: application/json" \

curl -X GET "https://clinicaltrials.gov/api/v2/studies" \
 -H "accept: application/json" > temp.json

from resultsSection.participantFlowModule.baselineCharacteristicsModule.measures.title = "Race (NIH/OMB)"
