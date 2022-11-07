from urllib.request import urlopen
from lxml import html
import requests
import asyncio

from src.objects import px500_xpaths
from src.modules.px500_parser import Px500Parser

local = "data/htmls/px500_popular"

urls_to_parse = ['https://drscdn.500px.org/photo/1056321491/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=83a895d7a4942f9d89061ce75b6b8f1473bcf8164116168314693dd85d746ad9',
                 'https://drscdn.500px.org/photo/1056312696/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=09eed7b4ab386650cc22b00b244089fb8a46ae5d2e09f0583755cd3eaff2f417',
                 'https://drscdn.500px.org/photo/1056328451/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=fa2e4c24c9aec7765f005d03aba84e7a2c9570a4b216244e4c774e222d829aea',
                 'https://drscdn.500px.org/photo/1056332663/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=be2cf00528d8077263cd2ca45b068df293ef2cadcf148faa47c659b2a2996edd',
                 'https://drscdn.500px.org/photo/1056328753/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=a0d6974ae193ae3a8f0f6fdf50e6f80e5a8f2218e56d87c6357fa56d276eba18',
                 'https://drscdn.500px.org/photo/1056321967/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=0a06cd9a44e60e1c01c1d1767ca0c6aff26e4333ab5d3ce8a6cdc5a56b7192d6',
                 'https://drscdn.500px.org/photo/1056311586/q%3D80_m%3D1500_k%3D1_of%3D1/v2?sig'
                 '=67ae1a8b56bf1616f713a1f849f0a2817bf9e509ccae1f02c1564a544ed01caa',
                 'https://drscdn.500px.org/photo/1056330631/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=a5f630b3e285ec598f837a8aba818f1344530078a2b6bc8a7f81f78bbb59ba93',
                 'https://drscdn.500px.org/photo/1056334952/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=52e356444816093c423accc2edd5c0dae4b53467e901876e64beafc119186664',
                 'https://drscdn.500px.org/photo/1056331372/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=cf625cf83b2e09dd64519e052314369f60815f1d096986c45a300feb95430997',
                 'https://drscdn.500px.org/photo/1056315244/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=4b77155fa909251db4c96c39ee45645d42a2c0551192eaf81818d9766210cb15',
                 'https://drscdn.500px.org/photo/1056334813/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=98695d4aba412a6b33482b256bdff7fe85f1718b6c9ae4dc2c939f0fb2209a63',
                 'https://drscdn.500px.org/photo/1056322823/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=4d41e6000eab25f06f10b0ae2d4e7bc7c0c9556edea428658ac51c27ae87ba25',
                 'https://drscdn.500px.org/photo/1056319026/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=ead75796939cde64fb0b861b7e8dae256b51f677467d02f22a4e13d9b5074235',
                 'https://drscdn.500px.org/photo/1056332558/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=873a3b10e0f02b65d385c89f290329e5a9e59a1880e1c8eb212fd0284a5a1e83',
                 'https://drscdn.500px.org/photo/1056331438/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=06145bd5bbfe4e118aadcfae3010137c985d7547751aa50acf6017d754e7d1a2',
                 'https://drscdn.500px.org/photo/1056333866/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=40fbc367b701f2132201ef91ad01a9922d8914df4060c2f399b289515632fc71',
                 'https://drscdn.500px.org/photo/1056335633/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=9bb57aa9bd0a86ef1c5f8979f47724d847b33ce6045a5ff7b57e281dce5af0f9',
                 'https://drscdn.500px.org/photo/1056326045/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=fa1aaded54bc0485ebe40b7ce3e94bf59eb8d2b33669f6d0db5af9bd5203d741',
                 'https://drscdn.500px.org/photo/1056330413/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=c9fdc07fee902527e3cc1b15b2b8bc46b6b1466726a434981e9688f5f58b788e',
                 'https://drscdn.500px.org/photo/1056335656/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=d9b49f3e566d1120a7e768100c307cfa80547a3eaaa522e02f4cfff221ed1c9e',
                 'https://drscdn.500px.org/photo/1056313568/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=2da5840e87900d95aa02816485d27158d0bffaf00eabc6131cef25bb62c571cf',
                 'https://drscdn.500px.org/photo/1056316693/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=f5b903b7aaa9294da31ee1516c40f5516e407c291b41bc233680037d28c5076a',
                 'https://drscdn.500px.org/photo/1056317702/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=e0b0b3fd3541c7ffb5b2dcc5818dc5c844bbb69ad57d75c035d4b42f69039e77',
                 'https://drscdn.500px.org/photo/1056326645/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=779a1693192a6aa43b5ac2307b00dfa3e4be1515f1e62dd9b1dd2754aab53b77',
                 'https://drscdn.500px.org/photo/1056322564/q%3D80_m%3D1500_k%3D1_of%3D1/v2?sig'
                 '=5d63131a7b0228a4db27d3b2a75ae8b28225bbec2584ba2539bff68ecb5f70f9',
                 'https://drscdn.500px.org/photo/1056316999/q%3D80_m%3D1500_k%3D1_of%3D1/v2?sig'
                 '=f48c92e6b620140bd8ed6f6c97d7aceba967336095e471dda5d05a9b2c98bd81',
                 'https://drscdn.500px.org/photo/1056334068/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=98997d9afcae31c6e9ca57aaf35a2c57f9dc4f02199d427ac4d0702cf8f01083',
                 'https://drscdn.500px.org/photo/1056330364/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=8a9b7d293c1ef113afc4f146ad3c1cf185474bf1ad118679ba40e8173a79182e',
                 'https://drscdn.500px.org/photo/1056315971/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=22b7a2053bb7fab4a5a858775fda590f3c0b911f745b107581d729f813f853be',
                 'https://drscdn.500px.org/photo/1056331552/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=a9235ac2fb1f46e65e8a4e2814b17cdcc7aa1532a0cbd7ea87a2824bc2b5a258',
                 'https://drscdn.500px.org/photo/1056348015/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=4114b60758c7e9367a351aa4b003efc5cd6544fff4e74db1834e0b1a742e9462',
                 'https://drscdn.500px.org/photo/1056334883/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=498ea0bac6486177b10c67a2ae9de9cf23636f347e2c7d569f49796a57b898ab',
                 'https://drscdn.500px.org/photo/1056331782/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=50b6e9020dc6aa9747efcb57f435ca05a8f5247c54dfeb29169905708bf0c518',
                 'https://drscdn.500px.org/photo/1056313855/q%3D80_m%3D1500_k%3D1_of%3D1/v2?sig'
                 '=c25be098f769e03f07a943e8f5ff4c131fa91ec23bc79f806732526f6e358abd',
                 'https://drscdn.500px.org/photo/1056331820/q%3D80_m%3D1500_k%3D1_of%3D1/v2?sig'
                 '=b746008b0a88b9b4836a1d1d071d4625596e53dcfcaf30bfbbd10216f9c7361e',
                 'https://drscdn.500px.org/photo/1056323169/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=6fc1a7f33f160bca1cc15f7322d5a0a90623047518c959e2fa9ca8626ef08241',
                 'https://drscdn.500px.org/photo/1056326313/q%3D80_m%3D1500_k%3D1_of%3D1/v2?sig'
                 '=9bf8ccac1614eb47717352e74fa7b73ad04144885f63697dbda2107c2db05aa3',
                 'https://drscdn.500px.org/photo/1056331898/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=fa107aba86c21673744448abaed33062fe5cb0c7fd1582e7ac1ed0a5fd8f2133',
                 'https://drscdn.500px.org/photo/1056332154/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=6314c7e5b989722059b0f4cd550030f393cd757ac7d8c72bb12a82e54a344207',
                 'https://drscdn.500px.org/photo/1056334360/q%3D80_m%3D1500_of%3D1/v2?sig'
                 '=9dae56af1966be4e46be273e57be973ada85465b1188e937f3dc3b6e3ec789eb']

# response = urlopen("file:///Users/ilyamanakinson/PycharmProjects/images_parser/data/htmls/px500_popular").read()
# tree = html.fromstring(response)
# picture = tree.xpath(px500_xpaths.picture)

praser = Px500Parser()

praser.parse_photo_url(['https://drscdn.500px.org/photo/1056321491/q%3D80_m%3D1500_of%3D1/v2?sig=83a895d7a4942f9d89061ce75b6b8f1473bcf8164116168314693dd85d746ad9'])