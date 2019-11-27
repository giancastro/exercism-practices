import re


class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    # Check valid input
    if input_string == "(;)":
        return SgfTree()

    VALUE_RE = r"(?:[A-Za-z\s]|\\.)+"
    PROPERTIE_RE = r"([A-Z]+)((?:\[{value}\])+)".format(value=VALUE_RE)
    SGF_RE = r"^\(;(?P<node>(?:{propertie})+)+(?P<children>(\(?;{propertie}\)?)*)?\)$".format(
        propertie=PROPERTIE_RE)

    try:
        sgf_match = re.match(SGF_RE, input_string)

        # Root
        node = re.findall(PROPERTIE_RE, sgf_match['node'])
        root = {}
        for propertie in node:
            key_ = propertie[0]
            value_ = re.findall(VALUE_RE, propertie[1])
            root[key_] = list(map(lambda i: i.replace(
                '\\', '').expandtabs(1), value_))

        # Child
        children = re.findall(PROPERTIE_RE, sgf_match['children'])
        child = []
        for propertie in children:
            key_ = propertie[0]
            value_ = re.findall(VALUE_RE, propertie[1])
            child.append(
                SgfTree({key_: list(map(lambda x: x.replace('\\', '').expandtabs(1), value_))}))

        return SgfTree(root, child)

    except Exception as error:
        raise ValueError(error)
