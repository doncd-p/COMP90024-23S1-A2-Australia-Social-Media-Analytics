var that;
class AsideBar {
  constructor(className) {
    // 导航主区域
    this.main = document.querySelector(className);
    // 侧边栏
    this.sideBarActive = this.main.querySelectorAll(".side-item-active");
    // 没有展开的侧边栏
    this.sideBarNotActive = this.main.querySelectorAll(".side-item");

    // 父导航
    this.parentSideActive = this.main.querySelectorAll(".parent-side-active");
    // 没有展开的父导航
    this.parentSideNotActive = this.main.querySelectorAll(".parent-side");
    // 子导航
    this.childSideActive = this.main.querySelectorAll(".child-item-active");
    // 没有展开的子导航
    this.childSideNotActive = this.main.querySelectorAll(".child-item");
    that = this;
    // 绑定事件
    this.init();
  }

  init() {
    // 绑定父导航样式切换
    for (var i = 0; i < this.sideBarActive.length; i++) {
      this.parentSideActive[i].onclick = this.toggleSide;
    }
    // 绑定子导航的样式切换
    for (var i = 0; i < this.childSideActive.length; i++) {
      this.childSideActive[i].onclick = this.toggleChildSide;
    }
    // 绑定未激活父导航的样式切换
    for (var i = 0; i < this.parentSideNotActive.length; i++) {
      this.parentSideNotActive[i].onclick = this.toggleSide;
    }
    // 绑定未激活子导航样式切换
    for (var i = 0; i < this.childSideNotActive.length; i++) {
      this.childSideNotActive[i].onclick = this.toggleChildSide;
    }
  }

  // 切换样式
  toggleSide() {
    var li = this.parentNode;
    // 获取父导航
    var parentNode = li.getElementsByTagName("div")[0];
    if (li.className === "side-item-active") {
      that.clearClass();
      // parentNode.className = "parent-side";
      // li.className = "side-item";
    } else {
      that.clearClass();
      li.className = "side-item-active";
      parentNode.className = "parent-side-active";
      // 选中当前导航栏下的子节点
      that.chooseChild(li);
    }
  }

  chooseChild(li) {
    var childNotActive = li.getElementsByTagName("li");
    for (var i = 0; i < childNotActive.length; i++) {
      childNotActive[i].className = "child-item-active";
    }
  }

  // 切换子导航样式
  toggleChildSide() {
    var child = this;
    if (child.className === "child-item-active") {
      child.className = "child-item";
      return;
    }
    child.className = "child-item-active";
  }

  // 清空所有父导航样式
  clearClass() {
    // 所有激活菜单对应的子导航栏样式
    var sideBarActiveChildActive =
      document.querySelectorAll(".child-item-active");
    // 将所有子导航栏设置为空
    for (var i = 0; i < sideBarActiveChildActive.length; i++) {
      sideBarActiveChildActive[i].className = "child-item";
    }
    // 所有激活的侧边栏样式对应的父导航
    var sideBarActiveParentActive = document.querySelectorAll(
      ".parent-side-active"
    );
    // 将所有父导航栏样式清空
    for (var i = 0; i < sideBarActiveParentActive.length; i++) {
      sideBarActiveParentActive[i].className = "parent-side";
    }
    // 所有的激活的侧边栏样式清空
    var sideBarActive = document.querySelectorAll(".side-item-active");
    // 将所有侧边栏样式清空
    for (var i = 0; i < sideBarActive.length; i++) {
      sideBarActive[i].className = "side-item";
    }
  }

  // 清空子导航样式
  clearChildClass() {
    var childSideActive = document.querySelectorAll(".child-item-active");
    for (var i = 0; i < childSideActive.length; i++) {
      childSideActive[i].className = "child-item";
    }
  }
}

var asideBar = new AsideBar(".sidebar");
