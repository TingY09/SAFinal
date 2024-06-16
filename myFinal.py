import streamlit as st

st.title("台灣經濟與犯罪率相關性分析")
st.subheader("軟體三411077029葉庭妤")
st.header(":one:動機與目的", divider='red')
st.subheader("動機")
st.write("近期常聽到民眾在網路平台提及薪水太少，跟不上物價上漲速度，思考相對變得負面。社會上對於薪資與物價之間的不平衡以及對經濟困境的擔憂已經引起了廣泛的關注，我想分析犯罪率與經濟發展之間的關係，尤其是在經濟不景氣和通貨膨脹情況下是否會導致犯罪率上升，又哪些型態的犯罪影響最為嚴重。")
st.subheader("目的")
st.write("1. 分析全國犯罪率與經濟成長率、失業率是否有正向關係。\n2. 找出哪些犯罪型態與經濟關係最密切。")
st.header(":two:資料來源", divider='orange')
st.write("A. 內政部警政署全球資訊網-重要統計結果表。\nB. 政府資料開放平台-年度國內主要經濟指標。")
st.link_button('前往A', 'https://www.npa.gov.tw/ch/app/data/doc?module=wg056&detailNo=991250337664864256&type=s')
st.link_button('前往B', 'https://apiservice.mol.gov.tw/OdService/download/A17000000J-030243-zbf')
st.header(":three:軟體需求分析與系統設計", divider='green')
st.subheader("使用案例圖")
st.image('useCase.png')
st.subheader("類別圖")
st.image('class.png')
st.header(":four:資料準備與處理", divider='violet')
st.write("1. 篩選取得資料，僅提取需要部份。\n2. 將資料中有缺失的部分進行調整。")
st.header(":five:分析方法與流程", divider='gray')
st.write("1. 分別計算經濟成長率、失業率與各項犯罪的相關係數。\n2. 比較兩者差異。")
st.header(":six:使用工具", divider='grey')
st.write("1. Streamlit。\n2. Excel。")
st.header(":seven:程式碼", divider='rainbow')
st.link_button('github', 'https://github.com/TingY09/SAFinal')



