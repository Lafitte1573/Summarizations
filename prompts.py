"""
您提供的评价标准列表已经很全面了，涵盖了摘要评估的各个方面。以下是对您提供的标准的进一步说明和补充：
**1. 准确度 (Accuracy)**:
* 摘要是否准确反映了新闻报道的内容？是否包含了所有关键信息，例如事件、人物、时间、地点等？
* 摘要是否避免了对原文内容的曲解或误读？
**2. 完整性 (Completeness)**:
* 摘要是否完整地概括了新闻报道的主要内容？是否遗漏了重要的细节或背景信息？
* 摘要是否能够让读者对新闻事件有一个全面而清晰的理解？
**3. 清晰度 (Clarity)**:
* 摘要是否清晰易懂？是否使用了简洁明了的语言，避免使用专业术语或过于复杂的句子结构？
* 摘要是否避免了歧义或模糊的表达？
**4. 连贯性 (Coherence)**:
* 摘要是否逻辑清晰，各部分之间衔接自然？是否使用了合适的过渡词或短语？
* 摘要是否避免了大跳跃或前后矛盾的情况？
**5. 简洁性 (Conciseness)**:
* 摘要是否简洁明了，没有冗余信息？是否能够用最少的文字表达最多的信息？
* 摘要是否避免了不必要的细节描述或重复内容？
**6. 相关性 (Relevance)**:
* 摘要是否与新闻报道的主题相关？是否突出了新闻报道的重点和亮点？
* 摘要是否能够吸引读者对新闻报道的兴趣？
**补充评价标准**：
* **客观性 (Objectivity)**: 摘要是否客观地反映了新闻报道的内容，避免加入主观评价或偏见？
* **新颖性 (Novelty)**: 摘要是否突出了新闻报道的新颖性或独特性，例如新的发现、新的观点等？
* **可读性 (Readability)**: 摘要是否易于阅读，例如使用了合适的句子长度、段落结构等？
**通过综合考虑这些评价标准，可以更全面地评估摘要的质量，并为其改进提供参考**。
"""

metrics = {
    '准确性': '摘要是否准确反映了新闻报道的内容？是否包含了所有关键信息，例如事件、人物、时间、地点等？摘要是否避免了对原文内容的曲解或误读？',
    '完整性': '摘要是否完整地概括了新闻报道的主要内容？是否遗漏了重要的细节或背景信息？摘要是否能够让读者对新闻事件有一个全面而清晰的理解？',
    '清晰度': '摘要是否清晰易懂？是否使用了简洁明了的语言，避免使用专业术语或过于复杂的句子结构？摘要是否避免了歧义或模糊的表达？',
    '连贯性': '摘要是否逻辑清晰，各部分之间衔接自然？是否使用了合适的过渡词或短语？摘要是否避免了大跳跃或前后矛盾的情况？',
    '简洁性': '摘要是否简洁明了，没有冗余信息？是否能够用最少的文字表达最多的信息？摘要是否避免了不必要的细节描述或重复内容？',
    '相关性': '摘要是否与新闻报道的主题相关？是否突出了新闻报道的重点和亮点？摘要是否能够吸引读者对新闻报道的兴趣？',
    '客观性': '摘要是否客观地反映了新闻报道的内容，避免加入主观评价或偏见？',
    '新颖性': '摘要是否突出了新闻报道的新颖性或独特性，例如新的发现、新的观点等？',
    '可读性': '摘要是否易于阅读，例如使用了合适的句子长度、段落结构等？'
}