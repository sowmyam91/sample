import xmltodict
import json
from pyhocon import HOCONConverter, ConfigFactory


class ConverterUtils:
    def __init__(self):
        self.tags = ('me', 'eq', 'eh', 'ptp')
        self.tag_list = []

    def filter_json(self, data, key='tmf854:vendorExtensions'):
        tag_dict = {}
        for tag in self.tags:
            self.find_key(data, tag)
            for t_data in self.tag_list:
                name_value = t_data.get(key, {}).get('package', None)

                if name_value:
                    if isinstance(name_value, dict):
                        name_value = [t_data[key]['package']]
                    modifed_data = ConverterUtils.modify_name_and_value(name_value)

                    t_data[key]['package'] = modifed_data

            tag_dict.update({tag: self.tag_list})
            self.tag_list = []
        return tag_dict

    @staticmethod
    def xml_to_json(xml_data):
        dict_data = xmltodict.parse(xml_data)
        return json.dumps(dict_data, indent=4)

    @staticmethod
    def modify_name_and_value(data):
        for t_data in data:
            keypair_dict = {}
            if isinstance(t_data, dict):
                if t_data.get('NameAndStringValue'):
                    # todo dict comprehension
                    for keypair in t_data.get('NameAndStringValue'):
                        keypair_dict.update({keypair["tmf854:name"]: keypair["tmf854:value"]})
                    t_data['NameAndStringValue'] = keypair_dict
        return data

    def find_key(self, data, f_key):
        if f_key in data.keys():
            self.tag_list.append(data.get(f_key))
        else:
            for key, value in data.items():
                if isinstance(value, dict):
                    value = self.find_key(value, f_key)
                    if value:
                        return value
                elif isinstance(value, list):
                    for item in value:
                        l_val = self.find_key(item, f_key)
                        if l_val:
                            return l_val
            return self.tag_list


class ToscaConverter:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def format_key(key, pattern=":"):
        return key.split(pattern)[1]

    @staticmethod
    def render_to_template(**data):
        config = ConfigFactory.from_dict(data)
        return HOCONConverter.convert(config, 'hocon')

    # @staticmethod
    # def get_data_properties(**data):
    #     if not isinstance(data, dict):
    #         return dict(type=type(data).__name__,
    #                              title=value,
    #                              desc=value,
    #                              optional=True
    #                              )
    #     else:
    #         return
    #
    #     return properties

    def convert_json_to_tosca(self):
        print(self.data)
        tempalte_args = []
        for k, v in self.data.iteritems():
            value = self.format_key(k)
            template_dict = dict(type=type(v).__name__,
                                 title=value,
                                 desc=value,
                                 optional=True
                                 )
            # if type(v).__name__ == "dict":
            #     properties = self.get_data_properties(**value)
            #     template_dict.update(properties=properties)
            tempalte_args.append({value: template_dict})

        tosca_data = {"tosca": tempalte_args}
        temp = ToscaConverter.render_to_template(**tosca_data)
        return temp


if __name__ == "__main__":
    with open('../data/001-http-response-getInventoryResponse.xml', 'r') as fd:
        xml_data = fd.read()
    json_data = ConverterUtils.xml_to_json(xml_data)

    with open('../data/sample.json', 'w') as f:
        f.write(json_data)
    json_data = json.loads(json_data)

    data = ConverterUtils().filter_json(json_data)

    with open('../data/sample1.json', 'w') as f:
        f.write(json.dumps(data, indent=4))

    me = ToscaConverter(data.get('me')[0]).convert_json_to_tosca()
    print me
