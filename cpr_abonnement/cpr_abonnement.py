# -- coding: utf-8 --
#
# Copyright (c) 2017, Magenta ApS
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

import re
import requests
from jinja2 import Template


ADD_PNR_SUBSCRIPTION = "AddPNRSubscription" 
REMOVE_PNR_SUBSCRIPTION = "RemovePNRSubscription"
GET_PNR_SUBSCRIPTIONS = "GetAllFilters" 


def pnr_all_subscribed(dependencies_dict, operation):
    """ get all cpr numbers using GetAllFilters
    """
    if operation == GET_PNR_SUBSCRIPTIONS:
        return invoke_operation(
            dependencies_dict=dependencies_dict,
            pnr=None,
            operation=operation
        )
    else:
        return 'Invalid operation. Use \'GetAllFilters\''


def pnr_subscription(dependencies_dict, pnr, operation):
    """The function serves as a facade to ease the interaction with
    Serviceplatformen's 'SF6002 - CPR Abonnement' service.
    The type of operation you want to perform depends on the type of operation
    that is assigned to the operation parameter key when calling the function.
    :param dependencies_dict:
    :param pnr: String of 10 digits -> r'^\d{10}$'
    :param operation: 'add' or 'remove'
    :type dependencies_dict:
    :type pnr: str
    :type operation: str
    :return: Response from the respective Serviceplatform web service operation
    invoked.
    :rtype: str"""

    is_cprnr_valid = validate_cprnr(pnr)

    if is_cprnr_valid:

        result = None

        if operation == ADD_PNR_SUBSCRIPTION:

            result = invoke_operation(
                dependencies_dict=dependencies_dict,
                pnr=pnr,
                operation=operation
            )

        elif operation == REMOVE_PNR_SUBSCRIPTION:

            result = invoke_operation(
                dependencies_dict=dependencies_dict,
                pnr=pnr,
                operation=operation
            )

        else:

            result = ('Invalid operation. Use \'AddPNRSubscription\'')
            ('or \'RemovePNRSubscription\'.')

        return result


def invoke_operation(dependencies_dict, pnr, operation):
    """The function is used to respectively invoke one of the two web service
    operations, 'AddPNRSubscription' or 'RemovePNRSubscription', from
    serviceplatformen's 'SF6002 - CPR Abonnement' service. It does this by
    constructing a SOAP envelope based on the type of operation assigned to
    the operation parameter key when calling the function.
    :param service_uuids: Serviceplatform invocation context uuids
    :param certificate: Path to Serviceplatform certificate
    :param cprnr: String of 10 digits -> r'^\d{10}$'
    :param operation: 'add' or 'get' or 'remove' - see servicespec
    :type service_uuids: dict
    :type certificate: str
    :type cprnr: str
    :type operation: str
    :return: Response from the respective Serviceplatform web service operation
    invoked.
    :rtype: str"""

    if operation in [ADD_PNR_SUBSCRIPTION, REMOVE_PNR_SUBSCRIPTION]:
        envelope_name = "SUBSCRIPTION"
        parameter_type = 'PNR'
    elif operation in [GET_PNR_SUBSCRIPTIONS]:
        envelope_name = "LIST_SUBSCRIBED"
        parameter_type = None
    else:
        return "Invalid operation, no matching envelope name"

    soap_envelope_template = dependencies_dict.get('soap_request_envelope')

    soap_envelope = construct_envelope_SF6002(
        template=soap_envelope_template,
        service_agreement=dependencies_dict.get('service_agreement'),
        system=dependencies_dict.get('system'),
        user=dependencies_dict.get('user'),
        service=dependencies_dict.get('service'),
        pnr=pnr,
        operation=operation,
        parameter_type=parameter_type,
        envelope_name=envelope_name
    )

    service_url = dependencies_dict.get('service_endpoint')

    certificate = dependencies_dict.get('certificate')

    try:

        response = requests.post(
            url=service_url,
            data=soap_envelope,
            cert=certificate
        )

        return response.text

    except requests.exceptions.RequestException as e:

        # TODO: Log exceptions to file, but where
        # to specify path to log file...? settings.py,
        # cpr_abonnement(path_to_log)...?
        # Log message: exceptions and ...?
        print('Exception Output: {}'.format(e))


def validate_cprnr(cprnr):

    if cprnr:

        check = re.match(r'^\d{10}$', cprnr)

        if check:

            return True

        else:

            # Log e.g. 'Not a valid cprnr'
            return False

    else:

        # Log e.g. 'Type error occured: input'
        return False


def construct_envelope_SF6002(
    template,
    service_agreement,
    system,
    user,
    service,
    pnr,
    operation,
    parameter_type,
    envelope_name="SUBSCRIPTION"


):
    """The function returnes a envelope for the service
    'SF6002 - CPR Abonnement'."""

    with open(template, "r") as filestream:
        template_string = filestream.read()

    xml_template = Template(template_string)

    populated_template = xml_template.render(
        pnr=pnr,
        service_agreement=service_agreement,
        system=system,
        user=user,
        service=service,
        operation=operation,
        parameter_type=parameter_type,
        envelope_name=envelope_name
    )

    # service platform requirement.
    latin_1_encoded_soap_envelope = populated_template.encode('latin-1')

    return latin_1_encoded_soap_envelope
