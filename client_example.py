# -- coding: utf-8 --
#
# Copyright (c) 2017, Magenta ApS
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

import json
import settings
import xmltodict

from time import sleep
from cpr_abonnement.cpr_abonnement import pnr_subscription

dependencies = {
    'service_endpoint': settings.SP_SERVICE_ENDPOINT,
    'certificate': settings.SP_CERTIFICATE,
    'soap_request_envelope': settings.SP_SOAP_REQUEST_ENVELOPE,
    'system': settings.SP_SYSTEM,
    'user': settings.SP_USER,
    'service_agreement': settings.SP_SERVICE_AGREEMENT,
    'service': settings.SP_SERVICE
}

"""Available service operations.
AddPNRSubscription or RemovePNRSubscription"""
operation = settings.ADD_PNR_SUBSCRIPTION

"""Example for working with a single pnr."""
# pnr = settings.PNR
# cpr_abonnement_response_envelope = pnr_subscription(
#     dependencies_dict=dependencies,
#     pnr=pnr,
#     operation=operation
# )
# print(cpr_abonnement_response_envelope)

"""Example of parsing a single pnr to a dict and extracting the response."""
# xml_to_dict = xmltodict.parse(cpr_abonnement_response_envelope)
#
# operation = 'ns3:{}Response'.format(operation)
#
# response_message = xml_to_dict['soap:Envelope']['soap:Body'][
#     operation]['ns3:Result']
# print(response_message)


"""Example on working with a list of pnr."""
added = 0
pnr_file = open(settings.PNR_LIST, 'r')
for pnr in pnr_file:
    cpr_abonnement_response_envelope = pnr_subscription(
        dependencies_dict=dependencies,
        pnr=pnr[:10],  # NOTE: Leaving out \n
        operation=operation
    )

    xml_to_dict = xmltodict.parse(cpr_abonnement_response_envelope)

    response_type_element = 'ns3:{}Response'.format(operation)
    response_message = xml_to_dict['soap:Envelope']['soap:Body'][
        response_type_element]['ns3:Result']

    if response_message == 'ADDED':
        added += 1

    print('{} {}'.format(added, response_message))
