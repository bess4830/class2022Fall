{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOwzPomLOZHPErFlR3c2KOn",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/bess4830/class2022Fall/blob/main/Test1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "wfL1qYBo5uil"
      },
      "outputs": [],
      "source": [
        "a = int(input())\n",
        "b = int(input())\n",
        "\n",
        "while(True) :\n",
        "  if i%2 == 0 :\n",
        "    a = a*1.07\n",
        "  else :\n",
        "    a = a + 10000\n",
        "\n",
        "  b = b*1.02\n",
        "\n",
        "  if a<b :\n",
        "    i = i+1\n",
        "  else :\n",
        "    break\n",
        "\n",
        "print(i)"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "CdTrFXMn6EUq"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}