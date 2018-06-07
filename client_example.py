# -- coding: utf-8 --
#
# Copyright (c) 2017, Magenta ApS
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

import settings
import xmltodict

from cpr_abonnement import pnr_subscription

dependencies = {
    'service_endpoint': settings.SP_SERVICE_ENDPOINT,
    'certificate': settings.SP_CERTIFICATE,
    'soap_request_envelope': settings.SP_SOAP_REQUEST_ENVELOPE,
    'system': settings.SP_SYSTEM,
    'user': settings.SP_USER,
    'service_agreement': settings.SP_SERVICE_AGREEMENT,
    'service': settings.SP_SERVICE
}

test_pnr = '0123456789'


# Choose either between 'AddPNRSubscription' or 'RemovePNRSubscription'.
operation = 'AddPNRSubscription'

cpr_abonnement_response_envelope = pnr_subscription(
    dependencies_dict=dependencies,
    pnr=test_pnr,
    operation=operation
)


xml_to_dict = xmltodict.parse(cpr_abonnement_response_envelope)

operation = 'ns2:{}Response'.format(operation)

result = xml_to_dict['soap:Envelope']['soap:Body'][
    operation]['ns2:Result']

print(cpr_abonnement_response_envelope)
