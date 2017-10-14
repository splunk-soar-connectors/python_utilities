# --
# File: python_utilities_connector.py
#
# --
# -----------------------------------------
# Phantom sample App Connector python file
# -----------------------------------------

# Phantom App imports
import phantom.app as phantom

from phantom.base_connector import BaseConnector
from phantom.action_result import ActionResult

# Imports local to this App
from python_utilities_consts import *
import simplejson as json
from datetime import datetime
import re
# import pprint
import inspect


def _json_fallback(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    else:
        return obj


# Define the App Class
class PhantomUtilitiesConnector(BaseConnector):

    def __init__(self):

        # Call the BaseConnectors init first
        super(PhantomUtilitiesConnector, self).__init__()

    # returns the python type of user provide item
    def _item_type(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))
        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        try:
            user_item = param[PYTHONUTILITIES_ITEM]
            result = type(user_item)
            action_result.add_data({'type': result})
            action_result.set_status(phantom.APP_SUCCESS)
        except Exception as e:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        return action_result.get_status()

    # returns a list from a dictionary through items() function
    def _dictionary_to_list(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))
        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        try:
            dictionary = param[PYTHONUTILITIES_ITEM]
            result = dictionary.items()
            action_result.add_data({'result': result})
            action_result.set_status(phantom.APP_SUCCESS)
        except Exception as e:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        return action_result.get_status()

    # returns the length of an item using len() function
    def _item_length(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))
        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        try:
            user_item = param[PYTHONUTILITIES_ITEM]
            result = len(user_item)
            action_result.add_data({'length': result})
            action_result.set_status(phantom.APP_SUCCESS)
        except Exception as e:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        return action_result.get_status()

    # returns the index of a substring in a string
    def _find_string(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))
        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        try:
            searchString = param[PYTHONUTILITIES_SEARCH_STRING]
            sourceString = param[PYTHONUTILITIES_SOURCE_STRING]
            start = 0
            end = len(sourceString)
            if PYTHONUTILITIES_SOURCE_STRING_START in param:
                start = int(param[PYTHONUTILITIES_SOURCE_STRING_START])
            if PYTHONUTILITIES_SOURCE_STRING_END in param:
                end = int(param[PYTHONUTILITIES_SOURCE_STRING_END])
            results_dict = {}

            result_index = sourceString.find(searchString, start, end)
            results_dict.update({'search_string_index': result_index})
            action_result.add_data(results_dict)
            action_result.set_status(phantom.APP_SUCCESS)
        except Exception as e:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        return action_result.get_status()

    # returns the length of an item using len() function
    def _split_string(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))
        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        try:
            source_string = param[PYTHONUTILITIES_SOURCE_STRING]
            result = source_string.split(PYTHONUTILITIES_SPLIT_VALUE)
            action_result.add_data({'list': result})
            action_result.set_status(phantom.APP_SUCCESS)
        except Exception as e:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        return action_result.get_status()

    # implements regex functions for manipulation
    def _re_function(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        # Set variables
        action = param[PYTHONUTILITIES_REGEX_ACTION]
        pattern = re.compile(param[PYTHONUTILITIES_REGEX_PATTERN])
        data = (param[PYTHONUTILITIES_SOURCE_STRING]).decode('utf8', 'replace')
        start = 0
        end = len(data) - 1

        if PYTHONUTILITIES_SOURCE_STRING_START in param:
            start = int(param[PYTHONUTILITIES_SOURCE_STRING_START])
        if PYTHONUTILITIES_SOURCE_STRING_END in param:
            end = int(param[PYTHONUTILITIES_SOURCE_STRING_END])
        if PYTHONUTILITIES_REGEX_REPLACE in param:
            if param[PYTHONUTILITIES_REGEX_REPLACE] == "''":
                replace = r''
            elif param[PYTHONUTILITIES_REGEX_REPLACE] == "' '":
                replace = r' '
            else:
                replace = param[PYTHONUTILITIES_REGEX_REPLACE]
        else:
            replace = r''

        # Set case structure for defined action
        if action == 'search':
            # Expected result is either string or unicode
            result = pattern.search(data, start, end)
        elif action == 'match':
            # Expected result is either string or unicode
            result = pattern.match(data, start, end)
        elif action == 'split':
            # Expected result is either string or unicode
            result = pattern.split(data)
        elif action == 'findall':
            # Expected result is list
            result = pattern.findall(data, start, end)
        elif action == 'finditer':
            # Expected result is iterator
            result = pattern.finditer(data, start, end)
        elif action == 'sub':
            # Expected result is either string or unicode
            result = pattern.sub(replace, data)
        elif action == 'subn':
            # Expected result is tuple
            result = pattern.subn(replace, data)
        else:
            action_results.set_status(phantom.APP_ERROR, 'Action not defined. Check requested action.')

        # Check to see if there are results then parse the type for formatting
        if result:
            action_result.set_status(phantom.APP_SUCCESS)
            self.debug_print("Type {}".format(type(result)))
            if isinstance(result, (str, unicode, list, dict, tuple)):
                if type(result) is dict:
                    action_result.add_data(result)
                elif type(result) is unicode:
                    self.debug_print("Unicode elif excuted")
                    result_dict = {
                        "result": result.encode('utf8', 'replace')
                    }
                    self.debug_print("{}".format(result_dict))
                    action_result.add_data(result_dict)
                else:
                    result_dict = {
                        "result": result
                    }
                    action_result.add_data(result_dict)
            else:
                action_result.add_data(result.groupdict())

        # action_result.update_summary({"type": str(type(result))})

        return action_result.get_status()

    def _get_substring(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        try:
            # Find a better way to validate the inputs. Especially if they are left blank.
            sourceString = param[PYTHONUTILITIES_SOURCE_STRING]
            start = 0
            end = len(sourceString) - 1
            step = 1
            if PYTHONUTILITIES_SOURCE_STRING_START in param:
                start = int(param[PYTHONUTILITIES_SOURCE_STRING_START])
            if PYTHONUTILITIES_SOURCE_STRING_END in param:
                end = int(param[PYTHONUTILITIES_SOURCE_STRING_END])
            if PYTHONUTILITIES_SOURCE_STRING_STEP in param:
                step = int(param[PYTHONUTILITIES_SOURCE_STRING_STEP])

            self.debug_print('string {}, start {}, end {}'.format(sourceString, start, end))
            sub_dict = {'substring': sourceString[start:end:step]}

            self.debug_print('substring {}'.format(sub_dict))
            action_result.add_data(sub_dict)
            action_result.set_status(phantom.APP_SUCCESS)
        except Exception as e:
            action_result.set_status(phantom.APP_ERROR, '', e)
            return action_result.get_status()

        return action_result.get_status()

    def _get_date(self, param):
        self.debug_print('{}'.format(inspect.stack()[0][3]))

        # Add an action result to the App Run
        action_result = ActionResult(dict(param))
        self.add_action_result(action_result)

        format_string = param.get('format_string', "%A, %d %B %Y %I:%M%p")

        # List of local time items
        local_dt = datetime.now()
        local_iso = local_dt.isocalendar()
        local_tt = local_dt.timetuple()
        local_time = {
            "local_year": local_tt[0],
            "local_month": local_tt[1],
            "local_day": local_tt[2],
            "local_hour": local_tt[3],
            "local_minute": local_tt[4],
            "local_second": local_tt[5],
            "local_weekday": local_tt[6],
            "local_day_number": local_tt[7],
            "local_tz": local_tt[8],
            "local_iso_week": local_iso[1],
            "local_iso_weekday": local_iso[2],
            "local_custom": local_dt.strftime(format_string)
        }

        # List of UTC time items
        utc_dt = datetime.utcnow()
        utc_iso = utc_dt.isocalendar()
        utc_tt = utc_dt.timetuple()
        utc_time = {
            "utc_year": utc_tt[0],
            "utc_month": utc_tt[1],
            "utc_day": utc_tt[2],
            "utc_hour": utc_tt[3],
            "utc_minute": utc_tt[4],
            "utc_second": utc_tt[5],
            "utc_weekday": utc_tt[6],
            "utc_day_number": utc_tt[7],
            "utc_tz": utc_tt[8],
            "utc_iso_week": utc_iso[1],
            "utc_iso_weekday": utc_iso[2],
            "utc_custom": utc_dt.strftime(format_string)
        }

        # Add time values to results
        action_result.add_data(local_time)
        action_result.add_data(utc_time)
        action_result.set_status(phantom.APP_SUCCESS)

        return action_result.get_status()

    def handle_action(self, param):

        ret_val = phantom.APP_SUCCESS
        action = self.get_action_identifier()
        self.debug_print("action_id", self.get_action_identifier())

        if (action == "find_string"):
            ret_val = self._find_string(param)
        elif (action == "item_type"):
            ret_val = self._item_type(param)
        elif (action == "dictionary_to_list"):
            ret_val = self._dictionary_to_list(param)
        elif (action == "item_length"):
            ret_val = self._item_length(param)
        elif (action == "split_string"):
            ret_val = self._split_string(param)
        elif (action == "get_substring"):
            ret_val = self._get_substring(param)
        elif (action == "regex_function"):
            ret_val = self._re_function(param)
        elif (action == "get_date"):
            ret_val = self._get_date(param)

        return ret_val


if __name__ == '__main__':

    import sys
    import pudb
    pudb.set_trace()

    if (len(sys.argv) < 2):
        print "No test json specified as input"
        exit(0)

    with open(sys.argv[1]) as f:
        in_json = f.read()
        in_json = json.loads(in_json)
        print(json.dumps(in_json, indent=4))

        connector = PythonUtilitiesConnector()
        connector.print_progress_message = True
        ret_val = connector._handle_action(json.dumps(in_json), None)
        print (json.dumps(json.loads(ret_val), indent=4))

    exit(0)
