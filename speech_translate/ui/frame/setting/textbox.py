from tkinter import ttk, font, Toplevel, Frame, LabelFrame, Text
from typing import Union

from arabic_reshaper import reshape
from bidi.algorithm import get_display
from matplotlib import pyplot as plt

from speech_translate._constants import PREVIEW_WORDS, APP_NAME
from speech_translate.ui.custom.checkbutton import CustomCheckButton
from speech_translate.ui.custom.combobox import ComboboxWithKeyNav
from speech_translate.ui.custom.spinbox import SpinboxNumOnly
from speech_translate.globals import sj, gc
from speech_translate.utils.helper import chooseColor, generate_color, emoji_img
from speech_translate.ui.custom.tooltip import tk_tooltip, tk_tooltips


class SettingTextbox:
    """
    Textboox tab in setting window.
    """
    def __init__(self, root: Toplevel, master_frame: Union[ttk.Frame, Frame]):
        self.root = root
        self.master = master_frame
        self.fonts = list(font.families())
        self.fonts.append("TKDefaultFont")
        self.fonts.sort()
        self.eye_emoji = emoji_img(16, "👀")

        # ------------------ Textbox ------------------
        self.f_tb_param = ttk.Frame(self.master)
        self.f_tb_param.pack(side="top", fill="both", expand=False)

        self.f_tb_1 = ttk.Frame(self.master)
        self.f_tb_1.pack(side="top", fill="x")

        self.f_tb_2 = ttk.Frame(self.master)
        self.f_tb_2.pack(side="top", fill="x")

        self.f_tb_param_1 = ttk.Frame(self.f_tb_param)
        self.f_tb_param_1.pack(side="top", fill="x")

        self.f_tb_param_2 = ttk.Frame(self.f_tb_param)
        self.f_tb_param_2.pack(side="top", fill="x")

        self.f_tb_param_3 = ttk.Frame(self.f_tb_param)
        self.f_tb_param_3.pack(side="top", fill="x")

        # -----
        self.lf_param_mw_tc = LabelFrame(self.f_tb_param_1, text="• Main Window Transcribed Speech")
        self.lf_param_mw_tc.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        self.f_mw_tc_1 = ttk.Frame(self.lf_param_mw_tc)
        self.f_mw_tc_1.pack(side="top", fill="x", pady=5, padx=5)

        self.f_mw_tc_2 = ttk.Frame(self.lf_param_mw_tc)
        self.f_mw_tc_2.pack(side="top", fill="x", pady=5, padx=5)

        self.f_mw_tc_3 = ttk.Frame(self.lf_param_mw_tc)
        self.f_mw_tc_3.pack(side="top", fill="x", pady=5, padx=5)

        self.f_mw_tc_4 = ttk.Frame(self.lf_param_mw_tc)
        self.f_mw_tc_4.pack(side="top", fill="x", pady=(0, 10), padx=5)

        self.lf_param_mw_tl = LabelFrame(self.f_tb_param_1, text="• Main Window Translated Speech")
        self.lf_param_mw_tl.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        self.f_mw_tl_1 = ttk.Frame(self.lf_param_mw_tl)
        self.f_mw_tl_1.pack(side="top", fill="x", pady=5, padx=5)

        self.f_mw_tl_2 = ttk.Frame(self.lf_param_mw_tl)
        self.f_mw_tl_2.pack(side="top", fill="x", pady=5, padx=5)

        self.f_mw_tl_3 = ttk.Frame(self.lf_param_mw_tl)
        self.f_mw_tl_3.pack(side="top", fill="x", pady=5, padx=5)

        self.f_mw_tl_4 = ttk.Frame(self.lf_param_mw_tl)
        self.f_mw_tl_4.pack(side="top", fill="x", pady=(0, 10), padx=5)

        self.lf_param_ex_tc = LabelFrame(self.f_tb_param_2, text="• Subtitle Window Transcribed Speech")
        self.lf_param_ex_tc.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        self.f_ex_tc_1 = ttk.Frame(self.lf_param_ex_tc)
        self.f_ex_tc_1.pack(side="top", fill="x", pady=5, padx=5)

        self.f_ex_tc_2 = ttk.Frame(self.lf_param_ex_tc)
        self.f_ex_tc_2.pack(side="top", fill="x", pady=5, padx=5)

        self.f_ex_tc_3 = ttk.Frame(self.lf_param_ex_tc)
        self.f_ex_tc_3.pack(side="top", fill="x", pady=5, padx=5)

        self.f_ex_tc_4 = ttk.Frame(self.lf_param_ex_tc)
        self.f_ex_tc_4.pack(side="top", fill="x", pady=5, padx=5)

        self.f_ex_tc_5 = ttk.Frame(self.lf_param_ex_tc)
        self.f_ex_tc_5.pack(side="top", fill="x", pady=(0, 10), padx=5)

        self.lf_param_ex_tl = LabelFrame(self.f_tb_param_2, text="• Subtitle Window Translated Speech")
        self.lf_param_ex_tl.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        self.f_ex_tl_1 = ttk.Frame(self.lf_param_ex_tl)
        self.f_ex_tl_1.pack(side="top", fill="x", pady=5, padx=5)

        self.f_ex_tl_2 = ttk.Frame(self.lf_param_ex_tl)
        self.f_ex_tl_2.pack(side="top", fill="x", pady=5, padx=5)

        self.f_ex_tl_3 = ttk.Frame(self.lf_param_ex_tl)
        self.f_ex_tl_3.pack(side="top", fill="x", pady=5, padx=5)

        self.f_ex_tl_4 = ttk.Frame(self.lf_param_ex_tl)
        self.f_ex_tl_4.pack(side="top", fill="x", pady=5, padx=5)

        self.f_ex_tl_5 = ttk.Frame(self.lf_param_ex_tl)
        self.f_ex_tl_5.pack(side="top", fill="x", pady=(0, 10), padx=5)

        # -----
        self.lf_param_other = LabelFrame(self.f_tb_param_3, text="• Other")
        self.lf_param_other.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        self.lf_confidence = ttk.LabelFrame(self.lf_param_other, text="• Confidence")
        self.lf_confidence.pack(side="left", fill="x", expand=False, padx=5, pady=5)

        self.f_confidence_1 = ttk.Frame(self.lf_confidence)
        self.f_confidence_1.pack(side="top", fill="x", pady=5, padx=5)

        self.lf_parsing = ttk.LabelFrame(self.lf_param_other, text="• Parsing")
        self.lf_parsing.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        self.f_parsing_1 = ttk.Frame(self.lf_parsing)
        self.f_parsing_1.pack(side="top", fill="x", pady=5, padx=5)
        # -------------
        # mw tc
        # 1
        self.lbl_mw_tc_max = ttk.Label(self.f_mw_tc_1, text="Max Length", width=16)
        self.lbl_mw_tc_max.pack(side="left", padx=5)
        self.spn_mw_tc_max = SpinboxNumOnly(
            self.root,
            self.f_mw_tc_1,
            1,
            5000,
            lambda x: sj.save_key("tb_mw_tc_max", int(x)) or self.preview_changes_tb(),
            initial_value=sj.cache["tb_mw_tc_max"],
            width=38
        )
        self.spn_mw_tc_max.pack(side="left", padx=5)
        self.cbtn_mw_tc_limit_max = CustomCheckButton(
            self.f_mw_tc_1,
            sj.cache["tb_mw_tc_limit_max"],
            lambda x: sj.save_key("tb_mw_tc_limit_max", x) or self.preview_changes_tb(),
            text="Enable",
            style="Switch.TCheckbutton"
        )
        self.cbtn_mw_tc_limit_max.pack(side="left", padx=5)

        # 2
        self.lbl_mw_tc_max_per_line = ttk.Label(self.f_mw_tc_2, text="Max Per Line", width=16)
        self.lbl_mw_tc_max_per_line.pack(side="left", padx=5)
        self.spn_mw_tc_max_per_line = SpinboxNumOnly(
            self.root,
            self.f_mw_tc_2,
            1,
            5000,
            lambda x: sj.save_key("tb_mw_tc_max_per_line", int(x)) or self.preview_changes_tb(),
            initial_value=sj.cache["tb_mw_tc_max_per_line"],
            width=38
        )
        self.spn_mw_tc_max_per_line.pack(side="left", padx=5)
        self.cbtn_mw_tc_limit_max_per_line = CustomCheckButton(
            self.f_mw_tc_2,
            sj.cache["tb_mw_tc_limit_max_per_line"],
            lambda x: sj.save_key("tb_mw_tc_limit_max_per_line", x) or self.preview_changes_tb(),
            text="Enable",
            style="Switch.TCheckbutton"
        )
        self.cbtn_mw_tc_limit_max_per_line.pack(side="left", padx=5)

        # 3
        self.lbl_mw_tc_font = ttk.Label(self.f_mw_tc_3, text="Font", width=16)
        self.lbl_mw_tc_font.pack(side="left", padx=5)
        self.cb_mw_tc_font = ComboboxWithKeyNav(self.f_mw_tc_3, values=self.fonts, state="readonly", width=30)
        self.cb_mw_tc_font.set(sj.cache["tb_mw_tc_font"])
        self.cb_mw_tc_font.pack(side="left", padx=5)
        self.cb_mw_tc_font.bind(
            "<<ComboboxSelected>>",
            lambda e: sj.save_key("tb_mw_tc_font", self.cb_mw_tc_font.get()) or self.preview_changes_tb(),
        )
        self.spn_mw_tc_font_size = SpinboxNumOnly(
            self.root,
            self.f_mw_tc_3,
            3,
            120,
            lambda x: sj.save_key("tb_mw_tc_font_size", int(x)) or self.preview_changes_tb(),
            initial_value=sj.cache["tb_mw_tc_font_size"],
            width=3
        )
        self.spn_mw_tc_font_size.pack(side="left", padx=5)
        tk_tooltip(self.spn_mw_tc_font_size, "Font Size")
        self.spn_mw_tc_font_size.pack(side="left", padx=5)
        self.cbtn_mw_tc_font_bold = CustomCheckButton(
            self.f_mw_tc_3,
            sj.cache["tb_mw_tc_font_bold"],
            lambda x: sj.save_key("tb_mw_tc_font_bold", x) or self.preview_changes_tb(),
            text="Bold",
            style="Switch.TCheckbutton"
        )
        self.cbtn_mw_tc_font_bold.pack(side="left", padx=5)

        self.cbtn_mw_tc_use_conf_color = CustomCheckButton(
            self.f_mw_tc_4,
            sj.cache["tb_mw_tc_use_conf_color"],
            lambda x: sj.save_key("tb_mw_tc_use_conf_color", x) or self.preview_changes_tb(),
            text="Colorize text based on confidence value when available"
        )
        self.cbtn_mw_tc_use_conf_color.pack(side="left", padx=5)

        # -------------
        # mw tl
        # 1
        self.lbl_mw_tl_max = ttk.Label(self.f_mw_tl_1, text="Max Length", width=16)
        self.lbl_mw_tl_max.pack(side="left", padx=5)
        self.spn_mw_tl_max = SpinboxNumOnly(
            self.root,
            self.f_mw_tl_1,
            1,
            5000,
            lambda x: sj.save_key("tb_mw_tl_max", int(x)) or self.preview_changes_tb(),
            initial_value=sj.cache["tb_mw_tl_max"],
            width=38
        )
        self.spn_mw_tl_max.pack(side="left", padx=5)
        self.cbtn_mw_tl_limit_max = CustomCheckButton(
            self.f_mw_tl_1,
            sj.cache["tb_mw_tl_limit_max"],
            lambda x: sj.save_key("tb_mw_tl_limit_max", x) or self.preview_changes_tb(),
            text="Enable",
            style="Switch.TCheckbutton"
        )
        self.cbtn_mw_tl_limit_max.pack(side="left", padx=5)

        # 2
        self.lbl_mw_tl_max_per_line = ttk.Label(self.f_mw_tl_2, text="Max Per Line", width=16)
        self.lbl_mw_tl_max_per_line.pack(side="left", padx=5)
        self.spn_mw_tl_max_per_line = SpinboxNumOnly(
            self.root,
            self.f_mw_tl_2,
            1,
            5000,
            lambda x: sj.save_key("tb_mw_tl_max_per_line", int(x)) or self.preview_changes_tb(),
            initial_value=sj.cache["tb_mw_tl_max_per_line"],
            width=38
        )
        self.spn_mw_tl_max_per_line.pack(side="left", padx=5)
        self.cbtn_mw_tl_limit_max_per_line = CustomCheckButton(
            self.f_mw_tl_2,
            sj.cache["tb_mw_tl_limit_max_per_line"],
            lambda x: sj.save_key("tb_mw_tl_limit_max_per_line", x) or self.preview_changes_tb(),
            text="Enable",
            style="Switch.TCheckbutton"
        )
        self.cbtn_mw_tl_limit_max_per_line.pack(side="left", padx=5)

        # 3
        self.lbl_mw_tl_font = ttk.Label(self.f_mw_tl_3, text="Font", width=16)
        self.lbl_mw_tl_font.pack(side="left", padx=5)
        self.cb_mw_tl_font = ComboboxWithKeyNav(self.f_mw_tl_3, values=self.fonts, state="readonly", width=30)
        self.cb_mw_tl_font.set(sj.cache["tb_mw_tl_font"])
        self.cb_mw_tl_font.pack(side="left", padx=5)
        self.cb_mw_tl_font.bind(
            "<<ComboboxSelected>>",
            lambda e: sj.save_key("tb_mw_tl_font", self.cb_mw_tl_font.get()) or self.preview_changes_tb(),
        )
        self.spn_mw_tl_font_size = SpinboxNumOnly(
            self.root,
            self.f_mw_tl_3,
            3,
            120,
            lambda x: sj.save_key("tb_mw_tl_font_size", int(x)) or self.preview_changes_tb(),
            initial_value=sj.cache["tb_mw_tl_font_size"],
            width=3
        )
        tk_tooltip(self.spn_mw_tl_font_size, "Font Size")
        self.spn_mw_tl_font_size.pack(side="left", padx=5)
        self.cbtn_mw_tl_font_bold = CustomCheckButton(
            self.f_mw_tl_3,
            sj.cache["tb_mw_tl_font_bold"],
            lambda x: sj.save_key("tb_mw_tl_font_bold", x) or self.preview_changes_tb(),
            text="Bold",
            style="Switch.TCheckbutton"
        )
        self.cbtn_mw_tl_font_bold.pack(side="left", padx=5)

        self.cbtn_mw_tl_use_conf_color = CustomCheckButton(
            self.f_mw_tl_4,
            sj.cache["tb_mw_tl_use_conf_color"],
            lambda x: sj.save_key("tb_mw_tl_use_conf_color", x) or self.preview_changes_tb(),
            text="Colorize text based on confidence value when available"
        )
        self.cbtn_mw_tl_use_conf_color.pack(side="left", padx=5)

        # -------------
        # detached tc
        # 1
        self.lbl_ex_tc_max = ttk.Label(self.f_ex_tc_1, text="Max Length", width=16)
        self.lbl_ex_tc_max.pack(side="left", padx=5)
        self.spn_ex_tc_max = SpinboxNumOnly(
            self.root,
            self.f_ex_tc_1,
            1,
            5000,
            lambda x: sj.save_key("tb_ex_tc_max", int(x)) or self.preview_changes_tb(),
            initial_value=sj.cache["tb_ex_tc_max"],
            width=38
        )
        self.spn_ex_tc_max.pack(side="left", padx=5)
        self.cbtn_ex_tc_limit_max = CustomCheckButton(
            self.f_ex_tc_1,
            sj.cache["tb_ex_tc_limit_max"],
            lambda x: sj.save_key("tb_ex_tc_limit_max", x) or self.preview_changes_tb(),
            text="Enable",
            style="Switch.TCheckbutton"
        )
        self.cbtn_ex_tc_limit_max.pack(side="left", padx=5)

        # 2
        self.lbl_ex_tc_max_per_line = ttk.Label(self.f_ex_tc_2, text="Max Per Line", width=16)
        self.lbl_ex_tc_max_per_line.pack(side="left", padx=5)
        self.spn_ex_tc_max_per_line = SpinboxNumOnly(
            self.root,
            self.f_ex_tc_2,
            1,
            5000,
            lambda x: sj.save_key("tb_ex_tc_max_per_line", int(x)) or self.preview_changes_tb(),
            initial_value=sj.cache["tb_ex_tc_max_per_line"],
            width=38
        )
        self.spn_ex_tc_max_per_line.pack(side="left", padx=5)
        self.cbtn_ex_tc_limit_max_per_line = CustomCheckButton(
            self.f_ex_tc_2,
            sj.cache["tb_ex_tc_limit_max_per_line"],
            lambda x: sj.save_key("tb_ex_tc_limit_max_per_line", x) or self.preview_changes_tb(),
            text="Enable",
            style="Switch.TCheckbutton"
        )
        self.cbtn_ex_tc_limit_max_per_line.pack(side="left", padx=5)

        # 3
        self.lbl_ex_tc_font = ttk.Label(self.f_ex_tc_3, text="Font", width=16)
        self.lbl_ex_tc_font.pack(side="left", padx=5)
        self.cb_ex_tc_font = ComboboxWithKeyNav(self.f_ex_tc_3, values=self.fonts, state="readonly", width=30)
        self.cb_ex_tc_font.set(sj.cache["tb_ex_tc_font"])
        self.cb_ex_tc_font.pack(side="left", padx=5)
        self.cb_ex_tc_font.bind(
            "<<ComboboxSelected>>",
            lambda e: sj.save_key("tb_ex_tc_font", self.cb_ex_tc_font.get()) or self.preview_changes_tb(),
        )
        self.spn_ex_tc_font_size = SpinboxNumOnly(
            self.root,
            self.f_ex_tc_3,
            3,
            120,
            lambda x: sj.save_key("tb_ex_tc_font_size", int(x)) or self.preview_changes_tb(),
            initial_value=sj.cache["tb_ex_tc_font_size"],
            width=3
        )
        tk_tooltip(self.spn_ex_tc_font_size, "Font Size")
        self.spn_ex_tc_font_size.pack(side="left", padx=5)
        self.cbtn_ex_tc_font_bold = CustomCheckButton(
            self.f_ex_tc_3,
            sj.cache["tb_ex_tc_font_bold"],
            lambda x: sj.save_key("tb_ex_tc_font_bold", x) or self.preview_changes_tb(),
            text="Bold",
            style="Switch.TCheckbutton"
        )
        self.cbtn_ex_tc_font_bold.pack(side="left", padx=5)

        # 4
        self.lbl_ex_tc_font_color = ttk.Label(self.f_ex_tc_4, text="Font Color", width=16)
        self.lbl_ex_tc_font_color.pack(side="left", padx=5)
        self.entry_ex_tc_font_color = ttk.Entry(self.f_ex_tc_4, width=10)
        self.entry_ex_tc_font_color.insert("end", sj.cache["tb_ex_tc_font_color"])
        self.entry_ex_tc_font_color.pack(side="left", padx=5)
        self.entry_ex_tc_font_color.bind(
            "<Button-1>",
            lambda e: chooseColor(self.entry_ex_tc_font_color, self.entry_ex_tc_font_color.get(), self.root) or sj.
            save_key("tb_ex_tc_font_color", self.entry_ex_tc_font_color.get()) or self.preview_changes_tb(),
        )
        self.entry_ex_tc_font_color.bind("<Key>", lambda e: "break")

        self.lbl_ex_tc_bg_color = ttk.Label(self.f_ex_tc_4, text="Background Color")
        self.lbl_ex_tc_bg_color.pack(side="left", padx=5)
        self.entry_ex_tc_bg_color = ttk.Entry(self.f_ex_tc_4, width=10)
        self.entry_ex_tc_bg_color.insert("end", sj.cache["tb_ex_tc_bg_color"])
        self.entry_ex_tc_bg_color.pack(side="left", padx=5)
        self.entry_ex_tc_bg_color.bind(
            "<Button-1>",
            lambda e: chooseColor(self.entry_ex_tc_bg_color, self.entry_ex_tc_bg_color.get(), self.root) or sj.
            save_key("tb_ex_tc_bg_color", self.entry_ex_tc_bg_color.get()) or self.preview_changes_tb(),
        )
        self.entry_ex_tc_bg_color.bind("<Key>", lambda e: "break")

        # 5
        self.cbtn_ex_tc_use_conf_color = CustomCheckButton(
            self.f_ex_tc_5,
            sj.cache["tb_ex_tc_use_conf_color"],
            lambda x: sj.save_key("tb_ex_tc_use_conf_color", x) or self.preview_changes_tb(),
            text="Colorize text based on confidence value when available"
        )
        self.cbtn_ex_tc_use_conf_color.pack(side="left", padx=5)

        # -------------
        # detached tl
        self.lbl_ex_tl_max = ttk.Label(self.f_ex_tl_1, text="Max Length", width=16)
        self.lbl_ex_tl_max.pack(side="left", padx=5)
        self.spn_ex_tl_max = SpinboxNumOnly(
            self.root,
            self.f_ex_tl_1,
            1,
            5000,
            lambda x: sj.save_key("tb_ex_tl_max", int(x)) or self.preview_changes_tb(),
            initial_value=sj.cache["tb_ex_tl_max"],
            width=38
        )
        self.spn_ex_tl_max.pack(side="left", padx=5)
        self.cbtn_ex_tl_limit_max = CustomCheckButton(
            self.f_ex_tl_1,
            sj.cache["tb_ex_tl_limit_max"],
            lambda x: sj.save_key("tb_ex_tl_limit_max", x) or self.preview_changes_tb(),
            text="Enable",
            style="Switch.TCheckbutton"
        )
        self.cbtn_ex_tl_limit_max.pack(side="left", padx=5)

        # 2
        self.lbl_ex_tl_max_per_line = ttk.Label(self.f_ex_tl_2, text="Max Per Line", width=16)
        self.lbl_ex_tl_max_per_line.pack(side="left", padx=5)
        self.spn_ex_tl_max_per_line = SpinboxNumOnly(
            self.root,
            self.f_ex_tl_2,
            1,
            5000,
            lambda x: sj.save_key("tb_ex_tl_max_per_line", int(x)) or self.preview_changes_tb(),
            initial_value=sj.cache["tb_ex_tl_max_per_line"],
            width=38
        )
        self.spn_ex_tl_max_per_line.pack(side="left", padx=5)
        self.cbtn_ex_tl_limit_max_per_line = CustomCheckButton(
            self.f_ex_tl_2,
            sj.cache["tb_ex_tl_limit_max_per_line"],
            lambda x: sj.save_key("tb_ex_tl_limit_max_per_line", x) or self.preview_changes_tb(),
            text="Enable",
            style="Switch.TCheckbutton"
        )
        self.cbtn_ex_tl_limit_max_per_line.pack(side="left", padx=5)

        # 3
        self.lbl_ex_tl_font = ttk.Label(self.f_ex_tl_3, text="Font", width=16)
        self.lbl_ex_tl_font.pack(side="left", padx=5)
        self.cb_ex_tl_font = ComboboxWithKeyNav(self.f_ex_tl_3, values=self.fonts, state="readonly", width=30)
        self.cb_ex_tl_font.set(sj.cache["tb_ex_tl_font"])
        self.cb_ex_tl_font.pack(side="left", padx=5)
        self.cb_ex_tl_font.bind(
            "<<ComboboxSelected>>",
            lambda e: sj.save_key("tb_ex_tl_font", self.cb_ex_tl_font.get()) or self.preview_changes_tb(),
        )
        self.spn_ex_tl_font_size = SpinboxNumOnly(
            self.root,
            self.f_ex_tl_3,
            3,
            120,
            lambda x: sj.save_key("tb_ex_tl_font_size", int(x)) or self.preview_changes_tb(),
            initial_value=sj.cache["tb_ex_tl_font_size"],
            width=3
        )
        tk_tooltip(self.spn_ex_tl_font_size, "Font Size")
        self.spn_ex_tl_font_size.pack(side="left", padx=5)
        self.cbtn_ex_tl_font_bold = CustomCheckButton(
            self.f_ex_tl_3,
            sj.cache["tb_ex_tl_font_bold"],
            lambda x: sj.save_key("tb_ex_tl_font_bold", x) or self.preview_changes_tb(),
            text="Bold",
            style="Switch.TCheckbutton"
        )
        self.cbtn_ex_tl_font_bold.pack(side="left", padx=5)

        # 4
        self.lbl_ex_tl_font_color = ttk.Label(self.f_ex_tl_4, text="Font Color", width=16)
        self.lbl_ex_tl_font_color.pack(side="left", padx=5)
        self.entry_ex_tl_font_color = ttk.Entry(self.f_ex_tl_4, width=10)
        self.entry_ex_tl_font_color.insert("end", sj.cache["tb_ex_tl_font_color"])
        self.entry_ex_tl_font_color.pack(side="left", padx=5)
        self.entry_ex_tl_font_color.bind(
            "<Button-1>",
            lambda e: chooseColor(self.entry_ex_tl_font_color, self.entry_ex_tl_font_color.get(), self.root) or sj.
            save_key("tb_ex_tl_font_color", self.entry_ex_tl_font_color.get()) or self.preview_changes_tb(),
        )
        self.entry_ex_tl_font_color.bind("<Key>", lambda e: "break")

        self.lbl_ex_tl_bg_color = ttk.Label(self.f_ex_tl_4, text="Background Color")
        self.lbl_ex_tl_bg_color.pack(side="left", padx=5)
        self.entry_ex_tl_bg_color = ttk.Entry(self.f_ex_tl_4, width=10)
        self.entry_ex_tl_bg_color.insert("end", sj.cache["tb_ex_tl_bg_color"])
        self.entry_ex_tl_bg_color.pack(side="left", padx=5)
        self.entry_ex_tl_bg_color.bind(
            "<Button-1>",
            lambda e: chooseColor(self.entry_ex_tl_bg_color, self.entry_ex_tl_bg_color.get(), self.root) or sj.
            save_key("tb_ex_tl_bg_color", self.entry_ex_tl_bg_color.get()) or self.preview_changes_tb(),
        )
        self.entry_ex_tl_bg_color.bind("<Key>", lambda e: "break")

        # 5
        self.cbtn_ex_tl_use_conf_color = CustomCheckButton(
            self.f_ex_tl_5,
            sj.cache["tb_ex_tl_use_conf_color"],
            lambda x: sj.save_key("tb_ex_tl_use_conf_color", x) or self.preview_changes_tb(),
            text="Colorize text based on confidence value when available"
        )
        self.cbtn_ex_tl_use_conf_color.pack(side="left", padx=5)

        # ------------------ Other ------------------
        self.lbl_gradient_low_conf = ttk.Label(self.f_confidence_1, text="Low Confidence", width=16)
        self.lbl_gradient_low_conf.pack(side="left", padx=5)

        self.entry_gradient_low_conf = ttk.Entry(self.f_confidence_1, width=10)
        self.entry_gradient_low_conf.insert("end", sj.cache["gradient_low_conf"])
        self.entry_gradient_low_conf.pack(side="left", padx=5)
        self.entry_gradient_low_conf.bind(
            "<Button-1>",
            lambda e: chooseColor(self.entry_gradient_low_conf, self.entry_gradient_low_conf.get(), self.root) or sj.
            save_key("gradient_low_conf", self.entry_gradient_low_conf.get()) or self.preview_changes_tb(),
        )
        self.entry_gradient_low_conf.bind("<Key>", lambda e: "break")

        self.lbl_gradient_high_conf = ttk.Label(self.f_confidence_1, text="High Confidence", width=16)
        self.lbl_gradient_high_conf.pack(side="left", padx=5)

        self.entry_gradient_high_conf = ttk.Entry(self.f_confidence_1, width=10)
        self.entry_gradient_high_conf.insert("end", sj.cache["gradient_high_conf"])
        self.entry_gradient_high_conf.pack(side="left", padx=5)
        self.entry_gradient_high_conf.bind(
            "<Button-1>",
            lambda e: chooseColor(self.entry_gradient_high_conf, self.entry_gradient_high_conf.get(), self.root) or sj.
            save_key("gradient_high_conf", self.entry_gradient_high_conf.get()) or self.preview_changes_tb(),
        )
        self.entry_gradient_high_conf.bind("<Key>", lambda e: "break")

        self.btn_preview_gradient = ttk.Button(
            self.f_confidence_1, image=self.eye_emoji, command=lambda: self.preview_gradient()
        )
        self.btn_preview_gradient.pack(side="left", padx=5)
        tk_tooltip(self.btn_preview_gradient, "Preview gradient")

        def keep_one_disabled(value: bool, other_widget: ttk.Checkbutton):
            if value:
                other_widget.configure(state="disabled")
            else:
                other_widget.configure(state="normal")

        self.cbtn_colorize_per_segment = CustomCheckButton(
            self.f_confidence_1,
            sj.cache["colorize_per_segment"],
            lambda x: sj.save_key("colorize_per_segment", x) or keep_one_disabled(x, self.cbtn_colorize_per_word),
            text="Colorize per segment",
            style="Switch.TCheckbutton"
        )
        self.cbtn_colorize_per_segment.pack(side="left", padx=5)
        tk_tooltip(
            self.cbtn_colorize_per_segment,
            "Check this option if you want to colorize the text based on the total probability value of words in each segment. "
            "This color will be set based on the color below",
        )

        self.cbtn_colorize_per_word = CustomCheckButton(
            self.f_confidence_1,
            sj.cache["colorize_per_word"],
            lambda x: sj.save_key("colorize_per_word", x) or keep_one_disabled(x, self.cbtn_colorize_per_segment),
            text="Colorize per word",
            style="Switch.TCheckbutton"
        )
        self.cbtn_colorize_per_word.pack(side="left", padx=5)
        tk_tooltip(
            self.cbtn_colorize_per_word,
            "Check this option if you want to colorize the text based on the probability value of each word. "
            "This color will be set based on the color below",
        )

        # on init disable the other option if one is enabled
        if sj.cache["colorize_per_segment"]:
            self.cbtn_colorize_per_word.configure(state="disabled")
        elif sj.cache["colorize_per_word"]:
            self.cbtn_colorize_per_segment.configure(state="disabled")

        self.cbtn_parse_arabic = CustomCheckButton(
            self.f_parsing_1,
            sj.cache["parse_arabic"],
            lambda x: sj.save_key("parse_arabic", x) or self.preview_changes_tb(),
            text="Parse Arabic character",
            style="Switch.TCheckbutton"
        )
        self.cbtn_parse_arabic.pack(side="left", padx=5, pady=(2, 3))
        tk_tooltip(
            self.cbtn_parse_arabic,
            "Check this option if you want to transcribe Arabic character. "
            "This will fix the display issue of Arabic character on tkinter textbox",
        )

        # ------------------ Preview ------------------
        # tb 1
        self.tb_preview_1 = Text(
            self.f_tb_1,
            height=3,
            width=27,
            wrap="word",
            font=(
                sj.cache["tb_mw_tc_font"],
                sj.cache["tb_mw_tc_font_size"],
                "bold" if sj.cache["tb_mw_tc_font_bold"] else "normal",
            ),
        )
        self.tb_preview_1.bind("<Key>", "break")
        self.tb_preview_1.pack(side="left", padx=5, pady=5, fill="both", expand=True)

        self.tb_preview_2 = Text(
            self.f_tb_1,
            height=3,
            width=27,
            wrap="word",
            font=(
                sj.cache["tb_mw_tl_font"],
                sj.cache["tb_mw_tl_font_size"],
                "bold" if sj.cache["tb_mw_tl_font_bold"] else "normal",
            ),
        )
        self.tb_preview_2.bind("<Key>", "break")
        self.tb_preview_2.insert("end", "TL Main window:\n" + PREVIEW_WORDS)
        self.tb_preview_2.pack(side="left", padx=5, pady=5, fill="both", expand=True)

        # tb 2
        self.tb_preview_3 = Text(
            self.f_tb_2,
            height=3,
            width=27,
            wrap="word",
            font=(
                sj.cache["tb_ex_tc_font"],
                sj.cache["tb_ex_tc_font_size"],
                "bold" if sj.cache["tb_ex_tc_font_bold"] else "normal",
            ),
            foreground=sj.cache["tb_ex_tc_font_color"],
            background=sj.cache["tb_ex_tc_bg_color"],
        )
        self.tb_preview_3.bind("<Key>", "break")
        self.tb_preview_3.insert("end", "TC Subtitle window:\n" + PREVIEW_WORDS)
        self.tb_preview_3.pack(side="left", padx=5, pady=5, fill="both", expand=True)

        self.tb_preview_4 = Text(
            self.f_tb_2,
            height=3,
            width=27,
            wrap="word",
            font=(
                sj.cache["tb_ex_tl_font"],
                sj.cache["tb_ex_tl_font_size"],
                "bold" if sj.cache["tb_ex_tl_font_bold"] else "normal",
            ),
            foreground=sj.cache["tb_ex_tl_font_color"],
            background=sj.cache["tb_ex_tl_bg_color"],
        )
        self.tb_preview_4.bind("<Key>", "break")
        self.tb_preview_4.insert("end", "TL Subtitle window:\n" + PREVIEW_WORDS)
        self.tb_preview_4.pack(side="left", padx=5, pady=5, fill="both", expand=True)

        # --------------------------
        # tooltips
        tk_tooltips(
            [
                self.lbl_mw_tc_max, self.spn_mw_tc_max, self.lbl_mw_tl_max, self.spn_mw_tl_max, self.lbl_ex_tc_max,
                self.spn_ex_tc_max, self.lbl_ex_tl_max, self.spn_ex_tl_max
            ],
            "Max character shown. Keep in mind that the result is also limited by "
            "the max buffer and max sentence in the record setting",
        )
        tk_tooltips(
            [
                self.lbl_mw_tc_max_per_line, self.spn_mw_tc_max_per_line, self.lbl_mw_tl_max_per_line,
                self.spn_mw_tl_max_per_line, self.lbl_ex_tc_max_per_line, self.spn_ex_tc_max_per_line,
                self.lbl_ex_tl_max_per_line, self.spn_ex_tl_max_per_line
            ],
            "Max character shown per line.\n\n"
            "Separator needs to contain a line break (\\n) for this to work",
        )
        tk_tooltips(
            [
                self.cbtn_mw_tc_limit_max, self.cbtn_mw_tc_limit_max_per_line, self.cbtn_mw_tl_limit_max,
                self.cbtn_mw_tl_limit_max_per_line, self.cbtn_ex_tc_limit_max, self.cbtn_ex_tc_limit_max_per_line,
                self.cbtn_ex_tl_limit_max, self.cbtn_ex_tl_limit_max_per_line
            ],
            "Enable character limit",
        )

        # --------------------------
        self.init_setting_once()

    # ------------------ Functions ------------------
    def init_setting_once(self):
        self.preview_changes_tb()

    def tb_delete(self):
        self.tb_preview_1.delete("1.0", "end")
        self.tb_preview_2.delete("1.0", "end")
        self.tb_preview_3.delete("1.0", "end")
        self.tb_preview_4.delete("1.0", "end")

    def tb_insert_preview(self):
        to_insert = PREVIEW_WORDS
        if sj.cache["parse_arabic"]:
            to_insert = str(get_display(reshape(to_insert)))

        self.tb_preview_1.insert("end", "TC Main window: " + to_insert)
        self.tb_preview_2.insert("end", "TL Main window: " + to_insert)
        self.tb_preview_3.insert("end", "TC Subtitle window: " + to_insert)
        self.tb_preview_4.insert("end", "TL Subtitle window: " + to_insert)

    def preview_changes_tb(self):
        if gc.mw is None:
            return

        self.tb_delete()
        self.tb_insert_preview()

        gc.mw.tb_transcribed.configure(
            font=(
                self.cb_mw_tc_font.get(),
                int(self.spn_mw_tc_font_size.get()),
                "bold" if self.cbtn_mw_tc_font_bold.instate(["selected"]) else "normal",
            )
        )
        self.tb_preview_1.configure(
            font=(
                self.cb_mw_tc_font.get(),
                int(self.spn_mw_tc_font_size.get()),
                "bold" if self.cbtn_mw_tc_font_bold.instate(["selected"]) else "normal",
            )
        )

        gc.mw.tb_translated.configure(
            font=(
                self.cb_mw_tl_font.get(),
                int(self.spn_mw_tl_font_size.get()),
                "bold" if self.cbtn_mw_tl_font_bold.instate(["selected"]) else "normal",
            )
        )
        self.tb_preview_2.configure(
            font=(
                self.cb_mw_tl_font.get(),
                int(self.spn_mw_tl_font_size.get()),
                "bold" if self.cbtn_mw_tl_font_bold.instate(["selected"]) else "normal",
            )
        )

        assert gc.ex_tcw is not None
        gc.ex_tcw.update_window_bg()
        self.tb_preview_3.configure(
            font=(
                self.cb_ex_tc_font.get(),
                int(self.spn_ex_tc_font_size.get()),
                "bold" if self.cbtn_ex_tc_font_bold.instate(["selected"]) else "normal",
            ),
            foreground=self.entry_ex_tc_font_color.get(),
            background=self.entry_ex_tc_bg_color.get(),
        )

        assert gc.ex_tlw is not None
        gc.ex_tlw.update_window_bg()
        self.tb_preview_4.configure(
            font=(
                self.cb_ex_tl_font.get(),
                int(self.spn_ex_tl_font_size.get()),
                "bold" if self.cbtn_ex_tl_font_bold.instate(["selected"]) else "normal",
            ),
            foreground=self.entry_ex_tl_font_color.get(),
            background=self.entry_ex_tl_bg_color.get(),
        )

    def preview_gradient(self):
        colors = [
            generate_color(i / 100, self.entry_gradient_low_conf.get(), self.entry_gradient_high_conf.get())
            for i in range(101)
        ]

        rgb_colors = [tuple(int(colors[i:i + 2], 16) for i in (1, 3, 5)) for colors in colors]

        plt.figure(figsize=(10, 5))
        plt.imshow([rgb_colors], interpolation="nearest", extent=[0, 1, 0, 1])  # type: ignore
        plt.title(
            f'Gradient Between {self.entry_gradient_low_conf.get()} as Low and {self.entry_gradient_high_conf.get()} as High'
        )
        plt.axis("off")
        # change window name
        if manager := plt.get_current_fig_manager():
            manager.set_window_title(
                f"Gradient Preview {self.entry_gradient_low_conf.get()} Low / {self.entry_gradient_high_conf.get()} High - {APP_NAME}"
            )
        plt.show()
