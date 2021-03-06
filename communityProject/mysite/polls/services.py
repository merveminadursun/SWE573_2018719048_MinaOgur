from .models import *
from qwikidata.sparql import (get_subclasses_of_item, return_sparql_query_results)
from qwikidata.entity import WikidataItem, WikidataLexeme, WikidataProperty
from qwikidata.linked_data_interface import get_entity_dict_from_api


class WikidataService:

    def query(query):
        # send any sparql query to the wikidata query service and get full result back
        # here we use an example that counts the number of humans
        # ?item rdfs:label "%s"@en.
        # SELECT  distinct ?item ?itemDescription
        # WHERE {
        # ?item rdfs: label ?itemDescription.
        #     FILTER(CONTAINS(LCASE(?itemDescription), "%s" @ en)).
        # }   limit 100

        sparql_query = """
       SELECT distinct ?item ?itemDescription WHERE{  
          ?item rdfs:label "%s"@en.
          SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }  
        }
        """ % query
        return return_sparql_query_results(sparql_query)


class UserService:

    def login(email, password):
        return MyUser.objects.filter(email=email, password=password).values()

    def signup(data):
        return MyUser.objects.filter(id=data.id).values()


class CommunityService:

    def getCommunity(url):
        return Community.objects.filter(url=url).values(
            'id',
            'name',
            'description',
            'creator__username',
            'date_created'
        )

    def getCommunityMembers(url):
        return Community.objects.filter(url=url).values(
            'members__id',
            'members__username',
            'members__date_registered'
        )

    def getCommunityDataTypes(url):
        return Community.objects.filter(url=url).values(
            'datatype__id',
            'datatype__title',
            'datatype__body'
        )

    def getCommunityDataFields(url):
        # todo is it possible to use Community here or should i use DataField model instead
        return Community.objects.filter(url=url).values(
            'datafield__id',
            'datafield__type__name',
            'datafield__is_required',
            'datafield__wikidata_item'
        )
        # data = Community.objects.filter(url=url).values(
        #    'id'
        # )
        # return DataField.objects.filter(id=data[0]).values()
