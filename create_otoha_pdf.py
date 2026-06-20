from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    KeepTogether,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


OUT = "output/pdf/otoha_june_mobile_report.pdf"
FONT = "/System/Library/Fonts/CJKSymbolsFallback.ttc"

pdfmetrics.registerFont(TTFont("AppFont", FONT))

styles = getSampleStyleSheet()
base = ParagraphStyle(
    "Base",
    parent=styles["BodyText"],
    fontName="AppFont",
    fontSize=9.2,
    leading=13,
    textColor=colors.HexColor("#26312d"),
)
small = ParagraphStyle(
    "Small",
    parent=base,
    fontSize=8,
    leading=11,
    textColor=colors.HexColor("#5f6b66"),
)
h1 = ParagraphStyle(
    "H1",
    parent=base,
    fontSize=20,
    leading=24,
    textColor=colors.HexColor("#26312d"),
    spaceAfter=8,
)
h2 = ParagraphStyle(
    "H2",
    parent=base,
    fontSize=13,
    leading=17,
    textColor=colors.HexColor("#26312d"),
    spaceBefore=10,
    spaceAfter=7,
)
h3 = ParagraphStyle(
    "H3",
    parent=base,
    fontSize=10.2,
    leading=13,
    textColor=colors.HexColor("#26312d"),
    spaceAfter=5,
)


plan = [
    ("월", "月", [
        ("아침", "朝", "소고기 애호박 진밥", "牛肉とズッキーニ風やわらかご飯", "밥 90g, 소고기 25g, 애호박 30g", "ご飯 90g、牛肉 25g、ズッキーニ風野菜 30g", "🥩"),
        ("점심", "昼", "닭감자조림과 양배추찜", "鶏じゃが煮とキャベツ蒸し", "밥 90g, 닭 30g, 감자 45g, 양배추 30g", "ご飯 90g、鶏肉 30g、じゃがいも 45g、キャベツ 30g", "🍗"),
        ("저녁", "夜", "두부 가지 덮밥", "豆腐となすの丼", "밥 85g, 두부 45g, 가지 35g", "ご飯 85g、豆腐 45g、なす 35g", "□"),
    ]),
    ("화", "火", [
        ("아침", "朝", "달걀 양파 죽", "卵と玉ねぎのお粥", "죽 150g, 달걀 1/2개, 양파 20g", "お粥 150g、卵 1/2個、玉ねぎ 20g", "🥚"),
        ("점심", "昼", "흰살생선 토마토 소스밥", "白身魚のトマトソースご飯", "밥 90g, 생선 30g, 토마토 35g", "ご飯 90g、魚 30g、トマト 35g", "🐟"),
        ("저녁", "夜", "돼지안심 양배추 볶음밥", "豚ヒレとキャベツの炒めご飯", "밥 90g, 돼지안심 30g, 양배추 35g", "ご飯 90g、豚ヒレ 30g、キャベツ 35g", "🐖"),
    ]),
    ("수", "水", [
        ("아침", "朝", "감자 브로콜리 수프", "じゃがいもとブロッコリーのスープ", "감자 60g, 우유 80ml, 브로콜리 25g", "じゃがいも 60g、牛乳 80ml、ブロッコリー 25g", "🥛"),
        ("점심", "昼", "두부 애호박 덮밥", "豆腐とズッキーニ風野菜の丼", "밥 90g, 두부 50g, 애호박 35g", "ご飯 90g、豆腐 50g、ズッキーニ風野菜 35g", "□"),
        ("저녁", "夜", "소고기 오이 무른비빔밥", "牛肉ときゅうりのやわらか混ぜご飯", "밥 90g, 소고기 25g, 오이 25g", "ご飯 90g、牛肉 25g、きゅうり 25g", "🥩"),
    ]),
    ("목", "木", [
        ("아침", "朝", "요거트 오트밀과 블루베리", "ヨーグルトオートミールとブルーベリー", "요거트 90g, 오트밀 20g, 블루베리 30g", "ヨーグルト 90g、オートミール 20g、ブルーベリー 30g", "🥛"),
        ("점심", "昼", "닭고기 가지찜 밥", "鶏肉となすの蒸しご飯", "밥 90g, 닭 30g, 가지 40g", "ご飯 90g、鶏肉 30g、なす 40g", "🍗"),
        ("저녁", "夜", "달걀 토마토 볶음밥", "卵とトマトの炒めご飯", "밥 85g, 달걀 1/2개, 토마토 40g", "ご飯 85g、卵 1/2個、トマト 40g", "🥚"),
    ]),
    ("금", "金", [
        ("아침", "朝", "양배추 달걀찜과 밥", "キャベツ入り茶碗蒸しとご飯", "밥 80g, 달걀 1/2개, 양배추 25g", "ご飯 80g、卵 1/2個、キャベツ 25g", "🥚"),
        ("점심", "昼", "고등어 감자조림", "さばとじゃがいもの煮物", "밥 90g, 고등어 25g, 감자 45g", "ご飯 90g、さば 25g、じゃがいも 45g", "🐟"),
        ("저녁", "夜", "두부 양파 소보로밥", "豆腐と玉ねぎのそぼろご飯", "밥 90g, 두부 50g, 양파 25g", "ご飯 90g、豆腐 50g、玉ねぎ 25g", "□"),
    ]),
    ("토", "土", [
        ("아침", "朝", "참외 치즈 토스트", "まくわうりとチーズトースト", "식빵 1/2장, 치즈 1/2장, 참외 50g", "食パン 1/2枚、チーズ 1/2枚、まくわうり 50g", "🥛"),
        ("점심", "昼", "소고기 토마토 리조또", "牛肉とトマトのリゾット", "밥 85g, 소고기 30g, 토마토 40g", "ご飯 85g、牛肉 30g、トマト 40g", "🥩"),
        ("저녁", "夜", "닭고기 애호박 국수", "鶏肉とズッキーニ風野菜のうどん", "면 80g, 닭 25g, 애호박 35g", "麺 80g、鶏肉 25g、ズッキーニ風野菜 35g", "🍗"),
    ]),
    ("일", "日", [
        ("아침", "朝", "감자 달걀 팬케이크", "じゃがいも卵パンケーキ", "감자 60g, 달걀 1/2개, 밀가루 8g", "じゃがいも 60g、卵 1/2個、小麦粉 8g", "🥚"),
        ("점심", "昼", "돼지안심 가지 덮밥", "豚ヒレとなすの丼", "밥 90g, 돼지안심 30g, 가지 35g", "ご飯 90g、豚ヒレ 30g、なす 35g", "🐖"),
        ("저녁", "夜", "두부 양배추 맑은국밥", "豆腐とキャベツの薄味スープご飯", "밥 80g, 두부 45g, 양배추 35g, 국물 60ml", "ご飯 80g、豆腐 45g、キャベツ 35g、スープ 60ml", "□"),
    ]),
]


def p(text, style=base):
    return Paragraph(text, style)


def make_table(data, widths, bg=colors.white):
    table = Table(data, colWidths=widths, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), "AppFont"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.3),
        ("LEADING", (0, 0), (-1, -1), 11),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#dfe7e1")),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8f3e5")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return table


story = []
doc = SimpleDocTemplate(
    OUT,
    pagesize=A4,
    rightMargin=12 * mm,
    leftMargin=12 * mm,
    topMargin=12 * mm,
    bottomMargin=12 * mm,
)

story.append(p("Otoha 6월 주간 유아식 리포트 / 6月 週間幼児食レポート", h1))
story.append(p("기간: 2026.06.22 - 2026.06.28 | 대상: Otoha, 23개월", base))
story.append(p("6월 추천: 애호박, 감자, 가지, 양파, 참외, 수박, 블루베리", small))
story.append(Spacer(1, 6))

story.append(p("이번 주 목표 / 今週の目標", h2))
goals = [
    ["제철 채소", "매일 2종 이상 노출", "旬の野菜", "毎日2種類以上"],
    ["철분", "소고기/돼지고기 3회 이상", "鉄分", "牛肉/豚肉を週3回以上"],
    ["단백질", "생선 2회, 두부 3회 이상", "たんぱく質", "魚2回、豆腐3回以上"],
    ["조리", "찜, 짧은 볶음, 저염", "調理", "蒸す、短時間炒め、薄味"],
]
story.append(make_table([[p(c, small) for c in row] for row in [["한국어", "내용", "日本語", "内容"]] + goals], [28*mm, 58*mm, 28*mm, 58*mm]))

story.append(p("그램수 기준 / グラム数の基準", h2))
story.append(make_table([
    [p("구분", small), p("기준", small), p("区分", small), p("基準", small)],
    [p("밥·죽·국물", small), p("조리 후 제공량", small), p("ご飯・お粥・スープ", small), p("調理後の提供量", small)],
    [p("고기·생선", small), p("손질 후 조리 전", small), p("肉・魚", small), p("下処理後、加熱前", small)],
    [p("채소·과일", small), p("껍질/씨 제거 후", small), p("野菜・果物", small), p("皮/種を除いた量", small)],
    [p("유제품·달걀", small), p("제공량 또는 개수", small), p("乳製品・卵", small), p("提供量または個数", small)],
], [32*mm, 54*mm, 32*mm, 54*mm]))

story.append(PageBreak())
story.append(p("요일별 3끼 식단 / 曜日別 3食献立", h2))

for day_ko, day_ja, meals in plan:
    rows = [[p(f"{day_ko} / {day_ja}", h3), p("메뉴 / 献立", h3), p("그램수 / 量", h3)]]
    for slot_ko, slot_ja, name_ko, name_ja, gram_ko, gram_ja, icon in meals:
        rows.append([
            p(f"{slot_ko}<br/>{slot_ja}", small),
            p(f"{icon} {name_ko}<br/>{name_ja}", small),
            p(f"{gram_ko}<br/>{gram_ja}", small),
        ])
    story.append(KeepTogether([make_table(rows, [23*mm, 76*mm, 75*mm]), Spacer(1, 6)]))

story.append(PageBreak())
story.append(p("초보자용 조리 원칙 / 初心者向け調理ポイント", h2))
recipe_rules = [
    ["재료 준비", "채소는 0.5cm 정도로 작게 자르고, 고기와 생선은 더 잘게 다집니다.", "材料準備", "野菜は約0.5cm、肉と魚はさらに細かくします。"],
    ["고기", "물 2-3큰술과 함께 중약불에서 분홍빛이 없어질 때까지 익힙니다.", "肉", "水大さじ2-3と一緒に中弱火でピンク色がなくなるまで加熱します。"],
    ["생선", "4-6분 익힌 뒤 살을 부수고 가시를 다시 확인합니다.", "魚", "4-6分加熱し、身をほぐして骨を確認します。"],
    ["달걀", "반숙 없이 완전히 익힙니다.", "卵", "半熟を残さず完全に火を通します。"],
    ["간", "기본은 무염, 필요 시 간장/된장 1-2방울 수준만 사용합니다.", "味付け", "基本は無塩、必要時だけ醤油/味噌をごく少量。"],
]
story.append(make_table([[p(c, small) for c in row] for row in [["한국어", "내용", "日本語", "内容"]] + recipe_rules], [28*mm, 58*mm, 28*mm, 58*mm]))

story.append(p("장보기 체크리스트 / 買い物チェックリスト", h2))
shopping = [
    ["쌀/밥", "생쌀 약 500g", "米/ご飯", "生米 約500g"],
    ["소고기", "구매 100g", "牛肉", "購入100g"],
    ["돼지안심", "구매 70-80g", "豚ヒレ", "購入70-80g"],
    ["닭고기", "구매 100g", "鶏肉", "購入100g"],
    ["흰살생선/고등어", "각 1회분", "白身魚/さば", "各1回分"],
    ["두부/달걀/요거트", "두부 190g, 달걀 2개, 요거트 90g", "豆腐/卵/ヨーグルト", "豆腐190g、卵2個、ヨーグルト90g"],
    ["채소", "감자, 양배추, 토마토, 가지, 애호박, 양파, 오이, 브로콜리", "野菜", "じゃがいも、キャベツ、トマト、なす、ズッキーニ風野菜、玉ねぎ、きゅうり、ブロッコリー"],
    ["과일", "참외 50g, 블루베리 30g", "果物", "まくわうり50g、ブルーベリー30g"],
]
story.append(make_table([[p(c, small) for c in row] for row in [["구분", "권장량", "区分", "目安量"]] + shopping], [31*mm, 58*mm, 31*mm, 56*mm]))

story.append(p("안전 주의 / 安全上の注意", h2))
story.append(p("포도·방울토마토는 세로 4등분, 견과류는 통째 제공 금지, 생선 가시는 완전히 제거합니다.<br/>ぶどう・ミニトマトは縦4等分、ナッツは丸ごと出さず、魚の骨は完全に取り除きます。", base))

doc.build(story)
print(OUT)
