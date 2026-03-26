"""
测试DuckDuckGo搜索工具集成
"""

import sys
import os


def test_simple_ddg():
    """简单测试DuckDuckGo搜索"""
    print("=" * 60)
    print("🦆 DuckDuckGo搜索简单测试")
    print("=" * 60)

    try:
        from langchain_community.tools import DuckDuckGoSearchRun
        from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

        print("\n✅ DuckDuckGo相关包导入成功！")

        wrapper = DuckDuckGoSearchAPIWrapper(region="wt-wt", max_results=3)
        print("✅ DuckDuckGo API包装器初始化成功")

        search_tool = DuckDuckGoSearchRun(api_wrapper=wrapper)
        print("✅ DuckDuckGo搜索工具创建成功")

        print("\n🔍 执行测试搜索: 'What is LangGraph?'")
        result = search_tool.invoke("What is LangGraph?")

        print(f"\n✅ 搜索成功！结果预览:")
        print("-" * 60)
        print(result[:500] + "..." if len(result) > 500 else result)
        print("-" * 60)

        return True

    except ImportError as e:
        print(f"\n❌ 导入失败: {e}")
        print("\n💡 请安装依赖:")
        print("   pip install langchain-community duckduckgo-search")
        return False
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        return False


if __name__ == "__main__":
    print("🦆 DeerFlow DuckDuckGo搜索集成测试\n")
    test_simple_ddg()
