from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


OUT = "output/pdf/otoha_june_share_report.pdf"
pdfmetrics.registerFont(TTFont("OtohaFont", "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"))


def style(name, font, size, leading, color="#26312d", **kw):
    return ParagraphStyle(name, fontName=font, fontSize=size, leading=leading, textColor=colors.HexColor(color), **kw)


ko = style("ko", "OtohaFont", 9.2, 13)
ko_small = style("ko_small", "OtohaFont", 8, 11, "#5f6b66")
ko_h1 = style("ko_h1", "OtohaFont", 21, 26, spaceAfter=8)
ko_h2 = style("ko_h2", "OtohaFont", 14, 18, spaceBefore=10, spaceAfter=7)
ja = style("ja", "OtohaFont", 9.2, 13)
ja_small = style("ja_small", "OtohaFont", 8, 11, "#5f6b66")
ja_h1 = style("ja_h1", "OtohaFont", 21, 26, spaceAfter=8)
ja_h2 = style("ja_h2", "OtohaFont", 14, 18, spaceBefore=10, spaceAfter=7)


def p(text, st):
    return Paragraph(text, st)


def table(rows, widths):
    t = Table(rows, colWidths=widths, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), "OtohaFont"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.2),
        ("LEADING", (0, 0), (-1, -1), 11),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#dfe7e1")),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8f3e5")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


ko_plan = [
    ("월", [("아침", "소고기 애호박 진밥", "밥 90g, 소고기 25g, 애호박 30g", "소고기"), ("점심", "닭감자조림과 양배추찜", "밥 90g, 닭 30g, 감자 45g, 양배추 30g", "닭고기"), ("저녁", "두부 가지 덮밥", "밥 85g, 두부 45g, 가지 35g", "두부")]),
    ("화", [("아침", "달걀 양파 죽", "죽 150g, 달걀 1/2개, 양파 20g", "달걀"), ("점심", "흰살생선 토마토 소스밥", "밥 90g, 생선 30g, 토마토 35g", "생선"), ("저녁", "돼지안심 양배추 볶음밥", "밥 90g, 돼지안심 30g, 양배추 35g", "돼지고기")]),
    ("수", [("아침", "감자 브로콜리 수프", "감자 60g, 우유 80ml, 브로콜리 25g", "유제품"), ("점심", "두부 애호박 덮밥", "밥 90g, 두부 50g, 애호박 35g", "두부"), ("저녁", "소고기 오이 무른비빔밥", "밥 90g, 소고기 25g, 오이 25g", "소고기")]),
    ("목", [("아침", "요거트 오트밀과 블루베리", "요거트 90g, 오트밀 20g, 블루베리 30g", "유제품"), ("점심", "닭고기 가지찜 밥", "밥 90g, 닭 30g, 가지 40g", "닭고기"), ("저녁", "달걀 토마토 볶음밥", "밥 85g, 달걀 1/2개, 토마토 40g", "달걀")]),
    ("금", [("아침", "양배추 달걀찜과 밥", "밥 80g, 달걀 1/2개, 양배추 25g", "달걀"), ("점심", "고등어 감자조림", "밥 90g, 고등어 25g, 감자 45g", "생선"), ("저녁", "두부 양파 소보로밥", "밥 90g, 두부 50g, 양파 25g", "두부")]),
    ("토", [("아침", "참외 치즈 토스트", "식빵 1/2장, 치즈 1/2장, 참외 50g", "유제품"), ("점심", "소고기 토마토 리조또", "밥 85g, 소고기 30g, 토마토 40g", "소고기"), ("저녁", "닭고기 애호박 국수", "면 80g, 닭 25g, 애호박 35g", "닭고기")]),
    ("일", [("아침", "감자 달걀 팬케이크", "감자 60g, 달걀 1/2개, 밀가루 8g", "달걀"), ("점심", "돼지안심 가지 덮밥", "밥 90g, 돼지안심 30g, 가지 35g", "돼지고기"), ("저녁", "두부 양배추 맑은국밥", "밥 80g, 두부 45g, 양배추 35g, 국물 60ml", "두부")]),
]

ja_plan = [
    ("月", [("朝", "牛肉とズッキーニ風やわらかご飯", "ご飯90g、牛肉25g、ズッキーニ風野菜30g", "牛肉"), ("昼", "鶏じゃが煮とキャベツ蒸し", "ご飯90g、鶏肉30g、じゃがいも45g、キャベツ30g", "鶏肉"), ("夜", "豆腐となすの丼", "ご飯85g、豆腐45g、なす35g", "豆腐")]),
    ("火", [("朝", "卵と玉ねぎのお粥", "お粥150g、卵1/2個、玉ねぎ20g", "卵"), ("昼", "白身魚のトマトソースご飯", "ご飯90g、魚30g、トマト35g", "魚"), ("夜", "豚ヒレとキャベツの炒めご飯", "ご飯90g、豚ヒレ30g、キャベツ35g", "豚肉")]),
    ("水", [("朝", "じゃがいもとブロッコリーのスープ", "じゃがいも60g、牛乳80ml、ブロッコリー25g", "乳製品"), ("昼", "豆腐とズッキーニ風野菜の丼", "ご飯90g、豆腐50g、ズッキーニ風野菜35g", "豆腐"), ("夜", "牛肉ときゅうりのやわらか混ぜご飯", "ご飯90g、牛肉25g、きゅうり25g", "牛肉")]),
    ("木", [("朝", "ヨーグルトオートミールとブルーベリー", "ヨーグルト90g、オートミール20g、ブルーベリー30g", "乳製品"), ("昼", "鶏肉となすの蒸しご飯", "ご飯90g、鶏肉30g、なす40g", "鶏肉"), ("夜", "卵とトマトの炒めご飯", "ご飯85g、卵1/2個、トマト40g", "卵")]),
    ("金", [("朝", "キャベツ入り茶碗蒸しとご飯", "ご飯80g、卵1/2個、キャベツ25g", "卵"), ("昼", "さばとじゃがいもの煮物", "ご飯90g、さば25g、じゃがいも45g", "魚"), ("夜", "豆腐と玉ねぎのそぼろご飯", "ご飯90g、豆腐50g、玉ねぎ25g", "豆腐")]),
    ("土", [("朝", "まくわうりとチーズトースト", "食パン1/2枚、チーズ1/2枚、まくわうり50g", "乳製品"), ("昼", "牛肉とトマトのリゾット", "ご飯85g、牛肉30g、トマト40g", "牛肉"), ("夜", "鶏肉とズッキーニ風野菜のうどん", "麺80g、鶏肉25g、ズッキーニ風野菜35g", "鶏肉")]),
    ("日", [("朝", "じゃがいも卵パンケーキ", "じゃがいも60g、卵1/2個、小麦粉8g", "卵"), ("昼", "豚ヒレとなすの丼", "ご飯90g、豚ヒレ30g、なす35g", "豚肉"), ("夜", "豆腐とキャベツの薄味スープご飯", "ご飯80g、豆腐45g、キャベツ35g、スープ60ml", "豆腐")]),
]


def add_language_section(story, lang):
    is_ko = lang == "ko"
    st = ko if is_ko else ja
    st_small = ko_small if is_ko else ja_small
    st_h1 = ko_h1 if is_ko else ja_h1
    st_h2 = ko_h2 if is_ko else ja_h2
    plan = ko_plan if is_ko else ja_plan
    story.append(p("Otoha 6월 주간 유아식 리포트" if is_ko else "Otoha 6月 週間幼児食レポート", st_h1))
    story.append(p("기간: 2026.06.22 - 2026.06.28 | 대상: Otoha, 23개월" if is_ko else "期間: 2026.06.22 - 2026.06.28 | 対象: Otoha, 23か月", st))
    story.append(p("6월 추천: 애호박, 감자, 가지, 양파, 참외, 수박, 블루베리" if is_ko else "6月おすすめ: ズッキーニ風野菜、じゃがいも、なす、玉ねぎ、まくわうり、すいか、ブルーベリー", st_small))
    story.append(p("이번 주 목표" if is_ko else "今週の目標", st_h2))
    goals = [
        ["제철 채소", "매일 2종 이상 노출"] if is_ko else ["旬の野菜", "毎日2種類以上"],
        ["철분", "소고기/돼지고기 3회 이상"] if is_ko else ["鉄分", "牛肉/豚肉を週3回以上"],
        ["단백질", "생선 2회, 두부 3회 이상"] if is_ko else ["たんぱく質", "魚2回、豆腐3回以上"],
        ["조리", "찜, 짧은 볶음, 저염"] if is_ko else ["調理", "蒸す、短時間炒め、薄味"],
    ]
    story.append(table([[p("목표" if is_ko else "目標", st_small), p("내용" if is_ko else "内容", st_small)]] + [[p(a, st_small), p(b, st_small)] for a, b in goals], [45*mm, 130*mm]))
    story.append(p("그램수 기준" if is_ko else "グラム数の基準", st_h2))
    basis = [
        ["밥·죽·국물", "조리 후 제공량"] if is_ko else ["ご飯・お粥・スープ", "調理後の提供量"],
        ["고기·생선", "손질 후 조리 전"] if is_ko else ["肉・魚", "下処理後、加熱前"],
        ["채소·과일", "껍질/씨 제거 후"] if is_ko else ["野菜・果物", "皮/種を除いた量"],
        ["유제품·달걀", "제공량 또는 개수"] if is_ko else ["乳製品・卵", "提供量または個数"],
    ]
    story.append(table([[p("구분" if is_ko else "区分", st_small), p("기준" if is_ko else "基準", st_small)]] + [[p(a, st_small), p(b, st_small)] for a, b in basis], [55*mm, 120*mm]))
    story.append(PageBreak())
    story.append(p("요일별 3끼 식단" if is_ko else "曜日別 3食献立", st_h2))
    for day, meals in plan:
        rows = [[p(day, st_small), p("시간" if is_ko else "時間", st_small), p("메뉴" if is_ko else "献立", st_small), p("양" if is_ko else "量", st_small), p("단백질" if is_ko else "たんぱく質", st_small)]]
        for slot, name, grams, protein in meals:
            rows.append([p("", st_small), p(slot, st_small), p(name, st_small), p(grams, st_small), p(protein, st_small)])
        story.append(KeepTogether([table(rows, [14*mm, 18*mm, 66*mm, 58*mm, 22*mm]), Spacer(1, 5)]))
    story.append(PageBreak())
    story.append(p("초보자용 조리 원칙" if is_ko else "初心者向け調理ポイント", st_h2))
    rules = [
        ["재료 준비", "채소는 0.5cm 정도로 작게 자르고, 고기와 생선은 더 잘게 다집니다."] if is_ko else ["材料準備", "野菜は約0.5cm、肉と魚はさらに細かくします。"],
        ["고기", "물 2-3큰술과 함께 중약불에서 분홍빛이 없어질 때까지 익힙니다."] if is_ko else ["肉", "水大さじ2-3と一緒に中弱火でピンク色がなくなるまで加熱します。"],
        ["생선", "4-6분 익힌 뒤 살을 부수고 가시를 다시 확인합니다."] if is_ko else ["魚", "4-6分加熱し、身をほぐして骨を確認します。"],
        ["달걀", "반숙 없이 완전히 익힙니다."] if is_ko else ["卵", "半熟を残さず完全に火を通します。"],
        ["간", "기본은 무염, 필요 시 간장/된장 1-2방울 수준만 사용합니다."] if is_ko else ["味付け", "基本は無塩、必要時だけ醤油/味噌をごく少量。"],
    ]
    story.append(table([[p("구분" if is_ko else "区分", st_small), p("내용" if is_ko else "内容", st_small)]] + [[p(a, st_small), p(b, st_small)] for a, b in rules], [38*mm, 137*mm]))
    story.append(p("장보기 체크리스트" if is_ko else "買い物チェックリスト", st_h2))
    shopping = [
        ["쌀/밥", "생쌀 약 500g"] if is_ko else ["米/ご飯", "生米 約500g"],
        ["소고기", "구매 100g"] if is_ko else ["牛肉", "購入100g"],
        ["돼지안심", "구매 70-80g"] if is_ko else ["豚ヒレ", "購入70-80g"],
        ["닭고기", "구매 100g"] if is_ko else ["鶏肉", "購入100g"],
        ["흰살생선/고등어", "각 1회분"] if is_ko else ["白身魚/さば", "各1回分"],
        ["두부/달걀/요거트", "두부 190g, 달걀 2개, 요거트 90g"] if is_ko else ["豆腐/卵/ヨーグルト", "豆腐190g、卵2個、ヨーグルト90g"],
        ["채소", "감자, 양배추, 토마토, 가지, 애호박, 양파, 오이, 브로콜리"] if is_ko else ["野菜", "じゃがいも、キャベツ、トマト、なす、ズッキーニ風野菜、玉ねぎ、きゅうり、ブロッコリー"],
        ["과일", "참외 50g, 블루베리 30g"] if is_ko else ["果物", "まくわうり50g、ブルーベリー30g"],
    ]
    story.append(table([[p("구분" if is_ko else "区分", st_small), p("권장량" if is_ko else "目安量", st_small)]] + [[p(a, st_small), p(b, st_small)] for a, b in shopping], [48*mm, 127*mm]))
    story.append(p("안전 주의" if is_ko else "安全上の注意", st_h2))
    story.append(p("포도·방울토마토는 세로 4등분, 견과류는 통째 제공 금지, 생선 가시는 완전히 제거합니다." if is_ko else "ぶどう・ミニトマトは縦4等分、ナッツは丸ごと出さず、魚の骨は完全に取り除きます。", st))


doc = SimpleDocTemplate(OUT, pagesize=A4, rightMargin=12*mm, leftMargin=12*mm, topMargin=12*mm, bottomMargin=12*mm)
story = []
add_language_section(story, "ko")
story.append(PageBreak())
add_language_section(story, "ja")
doc.build(story)
print(OUT)
