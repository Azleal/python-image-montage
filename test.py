import base64
import json

# Image.new('RGBA', size=(100,100), color=(255,255,255,0)).show()
# color = ImageColor.getrgb("gray")
#
# print(color)
import montage

base_path = "/Users/Azleal-Mac/Documents/workstation/pycharm-workspace/python-image-montage/images/"
images = list(map(lambda e: base_path + str(e) + ".jpg", range(1, 10)))

# GroupAvatarLayout().layout1().draw([images[0]])

# for i in range(1, 10):
#     image = GroupAvatarLayoutSet(5).get_layout(len(images[:i])).assemble(images[:i])
#     image.show()


def test_main_handler():
    images = [
        # "https://tenfei02.cfp.cn/creative/vcg/800/version23/VCG41175510742.jpg",
        # "https://alifei03.cfp.cn/creative/vcg/800/version23/VCG21154786fd8.jpg",
        "http://thirdqq.qlogo.cn/g?b=oidb&k=u35GtuyTWpMcBsgdgPsZTQ&s=100",
        "http://thirdwx.qlogo.cn/mmopen/dx4Y70y9XcvPtiaibdxYmvzno0DdicianENTIicsmb4f6s8TJ7CW5JbwiaibxEGoXcF1eSDaY3pJibJca2vdXw2dAhg7kw/132",
        "http://thirdwx.qlogo.cn/mmopen/YibYtvT3jEAfSowTlMZkD9Lr6cqsfGq5b9lAJkrjq3cHWyvl3uxSialZuZWO5wf4FXJq9fIIWFOZ0c01sEl5ITEISvOBY3EgTd/132",
        "http://thirdqq.qlogo.cn/g?b=oidb&k=u35GtuyTWpMcBsgdgPsZTQ&s=100",
        # "https://tenfei01.cfp.cn/creative/vcg/800/version23/VCG21e8edfadae.jpg"
    ]
    images_str = json.dumps(images)
    images_str_base64 = str(base64.urlsafe_b64encode(images_str.encode("utf-8")), encoding="utf-8")
    path = "/montage/layout_set/group_avatar/scale/5/images/%s" % images_str_base64
    print(path)
    event = {"path": path}
    result = montage.main_handler(event, None)
    print(result)


test_main_handler()