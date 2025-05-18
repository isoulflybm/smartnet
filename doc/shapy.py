from shapy.emulation.shaper import Shaper

ps = {("127.0.0.2",) : {'upload': 1024, 'download': 1024, 'delay': 56},
      ("127.0.0.3",) : {'upload': 256, 'download': 512, 'delay': 30},
      ("127.0.0.4",) : {'upload': 256, 'download': 512, 'delay': 30},
}

sh = Shaper()
sh.set_shaping(ps)
