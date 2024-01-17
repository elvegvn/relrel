import random
from datetime import datetime, timedelta

def sort_documents(documents):
    # 按时间戳对文档进行排序
    sorted_documents = sorted(documents, key=lambda x: datetime.datetime.strptime(x[' creation_time'], "%Y-%m-%d %H:%M:%S"))
    # 打印排序后的文档列表
    print(sorted_documents)

    # 按重要性对文档进行排序
    import random
    weights = [5, 3, 1]
    # 初始化重要性分数
    document_importances = [random.random() for _ in range(len(documents))]
    for i, document in enumerate(sorted_documents):
        # 计算当前文档的重要性分数
        current_importance = sum(document_importances[i])
        # 根据当前文档的重要性分数更新权重
        for j, weight in enumerate(weights):
            document_importances[i] *= (document_importances[i] + weight) / current_importance
            # 记录当前文档的权重
            document_importances[i] = current_importance
        # 对文档进行排序
        sorted_document_importances = sorted(document_importances, key=lambda x: x)
        # 打印排序后的文档列表
        print(sorted_document_importances)

# 示例：按照创建时间对文档进行排序
sort_documents(["文献1", "文献2", "文献3", "文献4", "文献5"])

# 示例：按照文档重要性对文档进行排序
sort_documents(["文献1", "文献2", "文献3", "文献4", "文献5"], weights=[5, 3, 1])
