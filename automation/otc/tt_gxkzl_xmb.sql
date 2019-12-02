/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50558
Source Host           : localhost:3306
Source Database       : python

Target Server Type    : MYSQL
Target Server Version : 50558
File Encoding         : 65001

Date: 2018-09-11 14:09:53
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for tt_gxkzl_xmb
-- ----------------------------
DROP TABLE IF EXISTS `tt_gxkzl_xmb`;
CREATE TABLE `tt_gxkzl_xmb` (
  `编号` int(11) DEFAULT NULL,
  `指标名称` varchar(100) DEFAULT NULL,
  `启用标志` varchar(100) DEFAULT NULL,
  `有效开始` varchar(100) DEFAULT NULL,
  `指标类型选择` varchar(100) DEFAULT NULL,
  `备注` varchar(100) DEFAULT NULL,
  `产品到期前N个交易日` varchar(100) DEFAULT NULL,
  `触警时操作` varchar(100) DEFAULT NULL,
  `管理人关联方` varchar(100) DEFAULT NULL,
  `托管行关联方` varchar(100) DEFAULT NULL,
  `委托人关联方` varchar(100) DEFAULT NULL,
  `投顾关联方` varchar(100) DEFAULT NULL,
  `购买其发行证券(产品)` varchar(100) DEFAULT NULL,
  `购买其主承销商证券` varchar(100) DEFAULT NULL,
  `和关联方互为交易对手` varchar(100) DEFAULT NULL,
  `购买其副承销商证券` varchar(100) DEFAULT NULL,
  `购买其承销团证券` varchar(100) DEFAULT NULL,
  `1触警时操作` varchar(100) DEFAULT NULL,
  `指令审批对应流程` varchar(100) DEFAULT NULL,
  `维度1` varchar(100) DEFAULT NULL,
  `维度2` varchar(100) DEFAULT NULL,
  `维度3` varchar(100) DEFAULT NULL,
  `上一日中债估值价` varchar(100) DEFAULT NULL,
  `上一日收盘价` varchar(100) DEFAULT NULL,
  `当前最新价` varchar(100) DEFAULT NULL,
  `上一日中债估值收益率` varchar(100) DEFAULT NULL,
  ` 上一日中债估值价` varchar(100) DEFAULT NULL,
  `1上一日收盘价` varchar(100) DEFAULT NULL,
  `1当前最新价` varchar(100) DEFAULT NULL,
  ` 1上一日中债估值价` varchar(100) DEFAULT NULL,
  `2当前最新价` varchar(100) DEFAULT NULL,
  ` 前收盘利率` varchar(100) DEFAULT NULL,
  ` 前加权平均利率` varchar(100) DEFAULT NULL,
  `当前加权平均利率` varchar(100) DEFAULT NULL,
  ` 最新利率` varchar(100) DEFAULT NULL,
  ` 基金公司加权平均利率` varchar(100) DEFAULT NULL,
  ` 3当前最新价` varchar(100) DEFAULT NULL,
  ` 1前收盘利率` varchar(100) DEFAULT NULL,
  `1前加权平均利率` varchar(100) DEFAULT NULL,
  `1当前加权平均利率` varchar(100) DEFAULT NULL,
  ` 1最新利率` varchar(100) DEFAULT NULL,
  `偏差：` varchar(100) DEFAULT NULL,
  `交易预警值（>=）：` varchar(100) DEFAULT NULL,
  `交易审批值（>=）：` varchar(100) DEFAULT NULL,
  `交易指令审批对应流程：` varchar(100) DEFAULT NULL,
  `交易违规值（>=）：` varchar(100) DEFAULT NULL,
  `ABS预警值（>=）：` varchar(100) DEFAULT NULL,
  `ABS审批值（>=）：` varchar(100) DEFAULT NULL,
  `ABS指令审批对应流程：` varchar(100) DEFAULT NULL,
  `ABS禁止值（>=）：` varchar(100) DEFAULT NULL,
  `1ABS禁止值（>=）：` varchar(100) DEFAULT NULL,
  `业务类别1` varchar(100) DEFAULT NULL,
  `业务类别2` varchar(100) DEFAULT NULL,
  `业务类别3` varchar(100) DEFAULT NULL,
  `控制方式：` varchar(100) DEFAULT NULL,
  `预警值 >=（%）：` varchar(100) DEFAULT NULL,
  `违规值 >=（%）：` varchar(100) DEFAULT NULL,
  `期限类型：` varchar(100) DEFAULT NULL,
  `控制范围：` varchar(100) DEFAULT NULL,
  `自定义维度1` varchar(100) DEFAULT NULL,
  `自定义维度2` varchar(100) DEFAULT NULL,
  `自定义维度3` varchar(100) DEFAULT NULL,
  `赎回权债券期限计算方式："` varchar(100) DEFAULT NULL,
  `利率跳升点数值(>=)：` varchar(100) DEFAULT NULL,
  `比较方式：` varchar(100) DEFAULT NULL,
  `期限预警值>=(天)：` varchar(100) DEFAULT NULL,
  `期限指令审批值>=(天)：` varchar(100) DEFAULT NULL,
  `期限违规值>=(天)：` varchar(100) DEFAULT NULL,
  `上市日为空时用申购日+n处理：` varchar(100) DEFAULT NULL,
  `产品到期日-限售日 预警值(<=)日：` varchar(100) DEFAULT NULL,
  `产品到期日-限售日 指令审批值(<=)日：` varchar(100) DEFAULT NULL,
  `产品到期日-限售日 违规值(<=)日：` varchar(100) DEFAULT NULL,
  `加权方式：` varchar(100) DEFAULT NULL,
  `组合自定义维度1` varchar(100) DEFAULT NULL,
  `组合自定义维度2` varchar(100) DEFAULT NULL,
  `组合自定义维度3` varchar(100) DEFAULT NULL,
  `组合自定义维度4` varchar(100) DEFAULT NULL,
  `组合自定义维度5` varchar(100) DEFAULT NULL,
  `久期的取数方案：` varchar(100) DEFAULT NULL,
  `久期预警值(>=)：` varchar(100) DEFAULT NULL,
  `久期指令审批值(>=)：` varchar(100) DEFAULT NULL,
  `久期违规值(>=)：` varchar(100) DEFAULT NULL,
  `控制预警值（>=）：` varchar(100) DEFAULT NULL,
  `控制审批值（>=）：` varchar(100) DEFAULT NULL,
  `控制指令审批对应流程：` varchar(100) DEFAULT NULL,
  `控制禁止值(>=)：` varchar(100) DEFAULT NULL,
  `投资范围类指标所在分组：1` varchar(100) DEFAULT NULL,
  `投资范围类指标所在分组：2` varchar(100) DEFAULT NULL,
  `交易对手类型：1` varchar(100) DEFAULT NULL,
  `交易对手类型：2` varchar(100) DEFAULT NULL,
  `交易对手类型：3` varchar(100) DEFAULT NULL,
  `交易对手类型：4` varchar(100) DEFAULT NULL,
  `交易对手类型：5` varchar(100) DEFAULT NULL,
  `交易所头寸（<=）：` varchar(100) DEFAULT NULL,
  `T+0头寸（<=）：` varchar(100) DEFAULT NULL,
  `T+1头寸（<=）：` varchar(100) DEFAULT NULL,
  `交易市场：1` varchar(100) DEFAULT NULL,
  `交易市场：2` varchar(100) DEFAULT NULL,
  `交易市场：3` varchar(100) DEFAULT NULL,
  `主体评级` varchar(100) DEFAULT NULL,
  `是否考虑指令未成：` varchar(100) DEFAULT NULL,
  `利率债券折算率(%)：` varchar(100) DEFAULT NULL,
  `信用债折算率(%)：` varchar(100) DEFAULT NULL,
  `债券基金折算率(%)：` varchar(100) DEFAULT NULL,
  `预警值(>= %)：` varchar(100) DEFAULT NULL,
  `指令审批值(>=%)：` varchar(100) DEFAULT NULL,
  `1指令审批对应流程：` varchar(100) DEFAULT NULL,
  `禁止值(>=%)：` varchar(100) DEFAULT NULL,
  `风险资产：1` varchar(100) DEFAULT NULL,
  `风险资产：2` varchar(100) DEFAULT NULL,
  `风险资产：3` varchar(100) DEFAULT NULL,
  `(M值)预警值(>=)：` varchar(100) DEFAULT NULL,
  `(M值)指令审批值(>=)：` varchar(100) DEFAULT NULL,
  `(M值)违规值(>=)：` varchar(100) DEFAULT NULL,
  `监控对象：` varchar(100) DEFAULT NULL,
  `控制方向：` varchar(100) DEFAULT NULL,
  `预警值（元）：` varchar(100) DEFAULT NULL,
  `审批值（元）：` varchar(100) DEFAULT NULL,
  `违规值（元）：` varchar(100) DEFAULT NULL,
  `(质押品公允价值/成交金额)预警值(>=)：` varchar(100) DEFAULT NULL,
  `质押品公允价值/成交金额)指令审批值(>=)：` varchar(100) DEFAULT NULL,
  `(质押品公允价值/成交金额)违规值(>=)：` varchar(100) DEFAULT NULL,
  `n值(前n大)：` varchar(100) DEFAULT NULL,
  `达标比例：` varchar(100) DEFAULT NULL,
  `现金分红` varchar(100) DEFAULT NULL,
  `配股` varchar(100) DEFAULT NULL,
  `?停牌` varchar(100) DEFAULT NULL,
  `?公告日` varchar(100) DEFAULT NULL,
  `登记日` varchar(100) DEFAULT NULL,
  `除权除息日` varchar(100) DEFAULT NULL,
  `投票日前N个交易日:` varchar(100) DEFAULT NULL,
  `股票市值占净值(>=n%):` varchar(100) DEFAULT NULL,
  `z产品到期前N个交易日:` varchar(100) DEFAULT NULL,
  `z单位净值范围:开始` varchar(100) DEFAULT NULL,
  `z单位净值范围:结束` varchar(100) DEFAULT NULL,
  `z T-1日单位净值范围:开始` varchar(100) DEFAULT NULL,
  `T-1日单位净值范围:开始` varchar(100) DEFAULT NULL,
  `"连续提醒N天:` varchar(100) DEFAULT NULL,
  `z证券类型：` varchar(100) DEFAULT NULL,
  `z行业控制：` varchar(100) DEFAULT NULL,
  `z预警值(>=)：` varchar(100) DEFAULT NULL,
  `z违规值(>=)：` varchar(100) DEFAULT NULL,
  `z控制层次` varchar(100) DEFAULT NULL,
  `z产品名称1` varchar(100) DEFAULT NULL,
  `z产品名称2` varchar(100) DEFAULT NULL,
  `z产品名称3` varchar(100) DEFAULT NULL,
  `z产品名称4` varchar(100) DEFAULT NULL,
  `z产品名称5` varchar(100) DEFAULT NULL,
  `z产品名称6` varchar(100) DEFAULT NULL,
  `z没有触警时是否记录日志` varchar(100) DEFAULT NULL,
  `z控制时间段` varchar(100) DEFAULT NULL,
  `z添加业务1` varchar(100) DEFAULT NULL,
  `z添加业务2` varchar(100) DEFAULT NULL,
  `z添加业务3` varchar(100) DEFAULT NULL,
  `z扫描时间段` varchar(100) DEFAULT NULL,
  `z扫描间隔` varchar(100) DEFAULT NULL,
  `z每个时间段最大提醒次数` varchar(100) DEFAULT NULL,
  `z提醒角色1` varchar(100) DEFAULT NULL,
  `z提醒角色2` varchar(100) DEFAULT NULL,
  `z事后巡检相关参数` varchar(100) DEFAULT NULL,
  `z高优先级指标1` varchar(100) DEFAULT NULL,
  `z高优先级指标2` varchar(100) DEFAULT NULL,
  `z低优先级指标1` varchar(100) DEFAULT NULL,
  `z低优先级指标2` varchar(100) DEFAULT NULL,
  `z指标1` varchar(100) DEFAULT NULL,
  `z指标2` varchar(100) DEFAULT NULL,
  `新增结果` varchar(100) DEFAULT NULL,
  `复核结果` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tt_gxkzl_xmb
-- ----------------------------
INSERT INTO `tt_gxkzl_xmb` VALUES ('0', 'str1[1]', 'str1[2]', 'str1[3]', 'str1[4]', 'str1[5]', 'str1[6]', 'str1[7]', 'str1[8]', 'str1[9]', 'str1[10]', 'str1[11]', 'str1[12]', 'str1[13]', 'str1[14]', 'str1[15]', 'str1[16]', 'str1[17]', 'str1[18]', 'str1[19]', 'str1[20]', 'str1[21]', 'str1[22]', 'str1[23]', 'str1[24]', 'str1[25]', 'str1[26]', 'str1[27]', 'str1[28]', 'str1[29]', 'str1[30]', 'str1[31]', 'str1[32]', 'str1[33]', 'str1[34]', 'str1[35]', 'str1[36]', 'str1[37]', 'str1[38]', 'str1[39]', 'str1[40]', 'str1[41]', 'str1[42]', 'str1[43]', 'str1[44]', 'str1[45]', 'str1[46]', 'str1[47]', 'str1[48]', 'str1[49]', 'str1[50]', 'str1[51]', 'str1[52]', 'str1[53]', 'str1[54]', 'str1[55]', 'str1[56]', 'str1[57]', 'str1[58]', 'str1[59]', 'str1[60]', 'str1[61]', 'str1[62]', 'str1[63]', 'str1[64]', 'str1[65]', 'str1[66]', 'str1[67]', 'str1[68]', 'str1[69]', 'str1[70]', 'str1[71]', 'str1[72]', 'str1[73]', 'str1[74]', 'str1[75]', 'str1[76]', 'str1[77]', 'str1[78]', 'str1[79]', 'str1[80]', 'str1[81]', 'str1[82]', 'str1[83]', 'str1[84]', 'str1[85]', 'str1[86]', 'str1[87]', 'str1[88]', 'str1[89]', 'str1[90]', 'str1[91]', 'str1[92]', 'str1[93]', 'str1[94]', 'str1[95]', 'str1[96]', 'str1[97]', 'str1[98]', 'str1[99]', 'str1[100]', 'str1[101]', 'str1[102]', 'str1[103]', 'str1[104]', 'str1[105]', 'str1[106]', 'str1[107]', 'str1[108]', 'str1[109]', 'str1[110]', 'str1[111]', 'str1[112]', 'str1[113]', 'str1[114]', 'str1[115]', 'str1[116]', 'str1[117]', 'str1[118]', 'str1[119]', 'str1[120]', 'str1[121]', 'str1[122]', 'str1[123]', 'str1[124]', 'str1[125]', 'str1[126]', 'str1[127]', 'str1[128]', 'str1[129]', 'str1[130]', 'str1[131]', 'str1[132]', 'str1[133]', 'str1[134]', 'str1[135]', 'str1[136]', 'str1[137]', 'str1[138]', 'str1[139]', 'str1[140]', 'str1[141]', 'str1[142]', 'str1[143]', 'str1[144]', 'str1[145]', 'str1[146]', 'str1[147]', 'str1[148]', 'str1[149]', 'str1[150]', 'str1[151]', 'str1[152]', 'str1[153]', 'str1[154]', 'str1[155]', 'str1[156]', 'str1[157]', 'str1[158]', 'str1[159]', 'str1[160]', 'str1[161]', 'str1[162]', 'str1[163]', 'str1[164]', '', '', null);
INSERT INTO `tt_gxkzl_xmb` VALUES ('1', '个性投资类1', '禁用', '2018-06-14', '同一行业债券、股票控制', '备注1', '', '2', '3', '3', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '股票', '万得三级', '10000', '50000', '基金', '创金合信货币（招行）', '创金合信鑫优选混合（招行）', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '4', '【专户】债券组合久期不得超过1年', '', '【专户】债券组合久期不得超过5年', '', '【专户】债券组合久期不得超过3年', '', '', '', null);
INSERT INTO `tt_gxkzl_xmb` VALUES ('2', '个性投资类2', '禁用', '2018-06-14', '新股打开涨停卖出提醒', '备注2', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '5', '', '', '', '', '管理组', '公募组', '系统管理组', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '4', '【专户】债券组合久期不得超过1年', '', '【专户】债券组合久期不得超过5年', '', '【专户】债券组合久期不得超过3年', '', '', '', null);
INSERT INTO `tt_gxkzl_xmb` VALUES ('3', '个性投资类3', '禁用', '2018-06-14', '禁止交易控制(事后)', '备注3', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '5', '10000', '100000', '20000', '80000', '', '', '', '', '', '管理组', '公募组', '系统管理组', '', '', '', '', '', '', '债券买入', '正回购', '买入', '', '', '', '', '', '4', '【专户】债券组合久期不得超过1年', '', '【专户】债券组合久期不得超过5年', '', '【专户】债券组合久期不得超过3年', '', '', '', null);
INSERT INTO `tt_gxkzl_xmb` VALUES ('4', '个性投资类4', '禁用', '2018-06-14', '投票预警控制', '备注4', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '3', '40', '', '', '', '', '', '', '', '', '', '', '管理组', '公募组', '系统管理组', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '4', '【专户】债券组合久期不得超过1年', '', '【专户】债券组合久期不得超过5年', '', '【专户】债券组合久期不得超过3年', '', '', '', null);
INSERT INTO `tt_gxkzl_xmb` VALUES ('5', '个性投资类5', '禁用', '2018-06-14', '公司行为控制', '备注5', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '现金分红', '配股', ' 停牌', ' 公告日', '登记日', '除权除息日', '', '', '', '', '', '', '', '', '', '', '', '', '基金', '创金合信货币（招行）', '创金合信鑫优选混合（招行）', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '4', '【专户】债券组合久期不得超过1年', '【公募】所有公募基金持有一家公司证券不超过总股本的10%', '【专户】债券组合久期不得超过5年', '【公募】股票资产占基金资产净值比例不高于95%（量化）', '【专户】债券组合久期不得超过3年', '【公募】卖出股指期货合约价值不得超过股票总市值的20%', '', '', null);
INSERT INTO `tt_gxkzl_xmb` VALUES ('6', '个性投资类6', '禁用', '2018-06-14', '投资者持仓份额集中度控制', '备注6', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '10', '6', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '管理组', '全公司', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '4', '【专户】债券组合久期不得超过1年', '【公募】所有公募基金持有一家公司证券不超过总股本的10%', '【专户】债券组合久期不得超过5年', '【公募】股票资产占基金资产净值比例不高于95%（量化）', '【专户】债券组合久期不得超过3年', '【公募】卖出股指期货合约价值不得超过股票总市值的20%', '', '', null);
INSERT INTO `tt_gxkzl_xmb` VALUES ('7', '个性投资类7', '禁用', '2018-06-14', '逆回购质押率水平监控', '备注7', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '2000', '3000', '4000', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '管理组', '全公司', '', '', '', '', '', '', '', '', '', '', '090000-100000|130000-150000', '2', '3', '风险管理员', '系统管理员', '4', '【专户】债券组合久期不得超过1年', '【公募】所有公募基金持有一家公司证券不超过总股本的10%', '【专户】债券组合久期不得超过5年', '【公募】股票资产占基金资产净值比例不高于95%（量化）', '【专户】债券组合久期不得超过3年', '【公募】卖出股指期货合约价值不得超过股票总市值的20%', '', '', null);
INSERT INTO `tt_gxkzl_xmb` VALUES ('8', '个性投资类8', '禁用', '2018-06-14', '止盈止损监控', '备注8', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '单位净值', '小于', '1000', '2000', '3000', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '基金', '创金合信货币（招行）', '创金合信鑫优选混合（招行）', '', '', '', '', '', '', '', '', '', '090000-100000|130000-150000', '2', '3', '风险管理员', '系统管理员', '', '【专户】债券组合久期不得超过1年', '', '【专户】债券组合久期不得超过5年', '', '【专户】债券组合久期不得超过3年', '', '', '', null);
INSERT INTO `tt_gxkzl_xmb` VALUES ('9', '个性投资类9', '禁用', '2018-06-14', '保本基金CPPI策略监控', '备注9', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '【昭尊】一年以下信用债', '到期日在一年以内的政府债券', '【昭尊】一年以上信用债', '1', '2', '3', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '管理组', '全公司', '', '', '', '', '', '', '', '', '', '', '090000-100000|130000-150000', '2', '3', '风险管理员', '系统管理员', '', '【专户】债券组合久期不得超过1年', '', '【专户】债券组合久期不得超过5年', '', '【专户】债券组合久期不得超过3年', '', '', '', null);
INSERT INTO `tt_gxkzl_xmb` VALUES ('10', '个性投资类10', '禁用', '2018-06-14', '交易所入库集中度控制（同一账户主体）', '备注10', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '上海证券交易所', '', '', 'AAA-', '是', '', '', '', '0.3', '0.4', '价格异常', '0.5', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '管理组', '公募组', '系统管理组', '', '', '', '', '', '', '', '', '', '090000-100000|130000-150000', '2', '3', '风险管理员', '系统管理员', '', '【专户】债券组合久期不得超过1年', '', '【专户】债券组合久期不得超过5年', '', '【专户】债券组合久期不得超过3年', '', '', '', null);
INSERT INTO `tt_gxkzl_xmb` VALUES (null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `tt_gxkzl_xmb` VALUES (null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `tt_gxkzl_xmb` VALUES (null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `tt_gxkzl_xmb` VALUES (null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null);
INSERT INTO `tt_gxkzl_xmb` VALUES (null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null);
