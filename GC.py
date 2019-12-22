#region Using declarations
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Input;
using System.Windows.Media;
using System.Xml.Serialization;
using NinjaTrader.Cbi;
using NinjaTrader.Gui;
using NinjaTrader.Gui.Chart;
using NinjaTrader.Gui.SuperDom;
using NinjaTrader.Gui.Tools;
using NinjaTrader.Data;
using NinjaTrader.NinjaScript;
using NinjaTrader.Core.FloatingPoint;
using NinjaTrader.NinjaScript.Indicators;
using NinjaTrader.NinjaScript.DrawingTools;
#endregion

//This namespace holds Strategies in this folder and is required. Do not change it. 
namespace NinjaTrader.NinjaScript.Strategies
{
	public class GeorgeClooney : Strategy
	{
		private PriceLine PriceLine2;
		private PriceLine PriceLine3;
		private PriceLine PriceLine1;
		private Series<bool> Resistance;
		private Series<bool> Support;

		protected override void OnStateChange()
		{
			if (State == State.SetDefaults)
			{
				Description									= @"Tring to make trends";
				Name										= "GeorgeClooney";
				Calculate									= Calculate.OnBarClose;
				EntriesPerDirection							= 20;
				EntryHandling								= EntryHandling.UniqueEntries;
				IsExitOnSessionCloseStrategy				= true;
				ExitOnSessionCloseSeconds					= 30;
				IsFillLimitOnTouch							= true;
				MaximumBarsLookBack							= MaximumBarsLookBack.TwoHundredFiftySix;
				OrderFillResolution							= OrderFillResolution.Standard;
				Slippage									= 0;
				StartBehavior								= StartBehavior.WaitUntilFlat;
				TimeInForce									= TimeInForce.Day;
				TraceOrders									= false;
				RealtimeErrorHandling						= RealtimeErrorHandling.StopCancelClose;
				StopTargetHandling							= StopTargetHandling.ByStrategyPosition;
				BarsRequiredToTrade							= 20;
				// Disable this property for performance gains in Strategy Analyzer optimizations
				// See the Help Guide for additional information
				IsInstantiatedOnEachOptimizationIteration	= true;
				Price					= 1;
			}
			else if (State == State.Configure)
			{
				AddDataSeries("ES 12-19", Data.BarsPeriodType.Minute, 1, Data.MarketDataType.Last);
			}
			else if (State == State.DataLoaded)
			{				
				Resistance = new Series<bool>(this);
				Support = new Series<bool>(this);			
				PriceLine2				= PriceLine(Close, false, false, true, 1, 1, 1);
				PriceLine3				= PriceLine(Close, false, false, true, 100, 100, 100);
				PriceLine1				= PriceLine(PriceLine2, false, false, true, 100, 100, 100);
				SetStopLoss(CalculationMode.Percent, 3);
			}
		}

		protected override void OnBarUpdate()
		{
			if (BarsInProgress != 0) 
				return;

			if (CurrentBars[0] < 15)
				return;

			 // Set 1
			if (PriceLine1[15] == PriceLine3[15])
			{
				EnterShortMIT(Convert.ToInt32(DefaultQuantity), Close[0], "");
			}
			
		}

		#region Properties
		[NinjaScriptProperty]
		[Range(1, int.MaxValue)]
		[Display(Name="Price", Order=1, GroupName="Parameters")]
		public int Price
		{ get; set; }
		#endregion

	}
}

#region Wizard settings, neither change nor remove
/*@
<?xml version="1.0"?>
<ScriptProperties xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <Calculate>OnBarClose</Calculate>
  <ConditionalActions>
    <ConditionalAction>
      <Actions>
        <WizardAction>
          <Children />
          <IsExpanded>false</IsExpanded>
          <IsSelected>true</IsSelected>
          <Name>Enter short position by a market-if-touched order</Name>
          <OffsetType>Arithmetic</OffsetType>
          <ActionProperties>
            <DashStyle>Solid</DashStyle>
            <DivideTimePrice>false</DivideTimePrice>
            <Id />
            <File />
            <IsAutoScale>false</IsAutoScale>
            <IsSimulatedStop>false</IsSimulatedStop>
            <IsStop>false</IsStop>
            <LogLevel>Information</LogLevel>
            <Mode>Currency</Mode>
            <OffsetType>Currency</OffsetType>
            <Priority>Medium</Priority>
            <Quantity>
              <DefaultValue>0</DefaultValue>
              <IsInt>true</IsInt>
              <DynamicValue>
                <Children />
                <IsExpanded>false</IsExpanded>
                <IsSelected>false</IsSelected>
                <Name>Default order quantity</Name>
                <OffsetType>Arithmetic</OffsetType>
                <AssignedCommand>
                  <Command>DefaultQuantity</Command>
                  <Parameters />
                </AssignedCommand>
                <BarsAgo>0</BarsAgo>
                <CurrencyType>Currency</CurrencyType>
                <Date>2019-12-21T18:49:14.6456262</Date>
                <DayOfWeek>Sunday</DayOfWeek>
                <EndBar>0</EndBar>
                <ForceSeriesIndex>false</ForceSeriesIndex>
                <LookBackPeriod>0</LookBackPeriod>
                <MarketPosition>Long</MarketPosition>
                <Period>0</Period>
                <ReturnType>Number</ReturnType>
                <StartBar>0</StartBar>
                <State>Undefined</State>
                <Time>0001-01-01T00:00:00</Time>
              </DynamicValue>
              <IsLiteral>false</IsLiteral>
              <LiveValue xsi:type="xsd:string">DefaultQuantity</LiveValue>
            </Quantity>
            <ServiceName />
            <ScreenshotPath />
            <SoundLocation />
            <StopPrice>
              <DefaultValue>0</DefaultValue>
              <IsInt>false</IsInt>
              <DynamicValue>
                <Children />
                <IsExpanded>false</IsExpanded>
                <IsSelected>true</IsSelected>
                <Name>Close</Name>
                <OffsetType>Arithmetic</OffsetType>
                <AssignedCommand>
                  <Command>{0}</Command>
                  <Parameters>
                    <string>Series1</string>
                    <string>BarsAgo</string>
                    <string>OffsetBuilder</string>
                  </Parameters>
                </AssignedCommand>
                <BarsAgo>0</BarsAgo>
                <CurrencyType>Currency</CurrencyType>
                <Date>2019-12-21T18:49:27.8119899</Date>
                <DayOfWeek>Sunday</DayOfWeek>
                <EndBar>0</EndBar>
                <ForceSeriesIndex>false</ForceSeriesIndex>
                <LookBackPeriod>0</LookBackPeriod>
                <MarketPosition>Long</MarketPosition>
                <Period>0</Period>
                <ReturnType>Series</ReturnType>
                <StartBar>0</StartBar>
                <State>Undefined</State>
                <Time>0001-01-01T00:00:00</Time>
              </DynamicValue>
              <IsLiteral>false</IsLiteral>
              <LiveValue xsi:type="xsd:string">Close[0]</LiveValue>
            </StopPrice>
            <Tag>
              <SeparatorCharacter> </SeparatorCharacter>
              <Strings>
                <NinjaScriptString>
                  <Index>0</Index>
                  <StringValue>Set Enter short position by a market-if-touched order</StringValue>
                </NinjaScriptString>
              </Strings>
            </Tag>
            <TextPosition>BottomLeft</TextPosition>
            <VariableDateTime>2019-12-21T18:49:14.6456262</VariableDateTime>
            <VariableBool>false</VariableBool>
          </ActionProperties>
          <ActionType>EnterMITorStop</ActionType>
          <Command>
            <Command>EnterShortMIT</Command>
            <Parameters>
              <string>quantity</string>
              <string>stopPrice</string>
              <string>signalName</string>
            </Parameters>
          </Command>
        </WizardAction>
      </Actions>
      <AnyOrAll>All</AnyOrAll>
      <Conditions>
        <WizardConditionGroup>
          <AnyOrAll>Any</AnyOrAll>
          <Conditions>
            <WizardCondition>
              <LeftItem xsi:type="WizardConditionItem">
                <Children />
                <IsExpanded>true</IsExpanded>
                <IsSelected>true</IsSelected>
                <Name>Close</Name>
                <OffsetType>Arithmetic</OffsetType>
                <AssignedCommand>
                  <Command>{0}</Command>
                  <Parameters>
                    <string>Series1</string>
                    <string>BarsAgo</string>
                    <string>OffsetBuilder</string>
                  </Parameters>
                </AssignedCommand>
                <BarsAgo>15</BarsAgo>
                <CurrencyType>Currency</CurrencyType>
                <Date>2019-12-21T16:04:34.8204001</Date>
                <DayOfWeek>Sunday</DayOfWeek>
                <EndBar>0</EndBar>
                <ForceSeriesIndex>false</ForceSeriesIndex>
                <LookBackPeriod>0</LookBackPeriod>
                <MarketPosition>Long</MarketPosition>
                <Period>0</Period>
                <ReturnType>Series</ReturnType>
                <Series1>
                  <AcceptableSeries>Indicator DataSeries CustomSeries DefaultSeries</AcceptableSeries>
                  <CustomProperties>
                    <item>
                      <key>
                        <string>ShowAskLine</string>
                      </key>
                      <value>
                        <anyType xsi:type="xsd:boolean">false</anyType>
                      </value>
                    </item>
                    <item>
                      <key>
                        <string>ShowBidLine</string>
                      </key>
                      <value>
                        <anyType xsi:type="xsd:boolean">false</anyType>
                      </value>
                    </item>
                    <item>
                      <key>
                        <string>ShowLastLine</string>
                      </key>
                      <value>
                        <anyType xsi:type="xsd:boolean">true</anyType>
                      </value>
                    </item>
                    <item>
                      <key>
                        <string>AskLineLength</string>
                      </key>
                      <value>
                        <anyType xsi:type="NumberBuilder">
                          <DefaultValue>0</DefaultValue>
                          <IsInt>true</IsInt>
                          <IsLiteral>true</IsLiteral>
                          <LiveValue xsi:type="xsd:string">100</LiveValue>
                        </anyType>
                      </value>
                    </item>
                    <item>
                      <key>
                        <string>BidLineLength</string>
                      </key>
                      <value>
                        <anyType xsi:type="NumberBuilder">
                          <DefaultValue>0</DefaultValue>
                          <IsInt>true</IsInt>
                          <IsLiteral>true</IsLiteral>
                          <LiveValue xsi:type="xsd:string">100</LiveValue>
                        </anyType>
                      </value>
                    </item>
                    <item>
                      <key>
                        <string>LastLineLength</string>
                      </key>
                      <value>
                        <anyType xsi:type="NumberBuilder">
                          <DefaultValue>0</DefaultValue>
                          <IsInt>true</IsInt>
                          <IsLiteral>true</IsLiteral>
                          <LiveValue xsi:type="xsd:string">100</LiveValue>
                        </anyType>
                      </value>
                    </item>
                  </CustomProperties>
                  <IndicatorHolder>
                    <IndicatorName>PriceLine</IndicatorName>
                    <Plots />
                  </IndicatorHolder>
                  <IsExplicitlyNamed>false</IsExplicitlyNamed>
                  <IsPriceTypeLocked>false</IsPriceTypeLocked>
                  <PlotOnChart>false</PlotOnChart>
                  <PriceType>Close</PriceType>
                  <SeriesType>Indicator</SeriesType>
                  <HostedDataSeries>
                    <AcceptableSeries>Indicator DataSeries CustomSeries DefaultSeries</AcceptableSeries>
                    <CustomProperties>
                      <item>
                        <key>
                          <string>ShowAskLine</string>
                        </key>
                        <value>
                          <anyType xsi:type="xsd:boolean">false</anyType>
                        </value>
                      </item>
                      <item>
                        <key>
                          <string>ShowBidLine</string>
                        </key>
                        <value>
                          <anyType xsi:type="xsd:boolean">false</anyType>
                        </value>
                      </item>
                      <item>
                        <key>
                          <string>ShowLastLine</string>
                        </key>
                        <value>
                          <anyType xsi:type="xsd:boolean">true</anyType>
                        </value>
                      </item>
                      <item>
                        <key>
                          <string>AskLineLength</string>
                        </key>
                        <value>
                          <anyType xsi:type="NumberBuilder">
                            <DefaultValue>0</DefaultValue>
                            <IsInt>true</IsInt>
                            <IsLiteral>true</IsLiteral>
                            <LiveValue xsi:type="xsd:string">1</LiveValue>
                          </anyType>
                        </value>
                      </item>
                      <item>
                        <key>
                          <string>BidLineLength</string>
                        </key>
                        <value>
                          <anyType xsi:type="NumberBuilder">
                            <DefaultValue>0</DefaultValue>
                            <IsInt>true</IsInt>
                            <IsLiteral>true</IsLiteral>
                            <LiveValue xsi:type="xsd:string">1</LiveValue>
                          </anyType>
                        </value>
                      </item>
                      <item>
                        <key>
                          <string>LastLineLength</string>
                        </key>
                        <value>
                          <anyType xsi:type="NumberBuilder">
                            <DefaultValue>0</DefaultValue>
                            <IsInt>true</IsInt>
                            <IsLiteral>true</IsLiteral>
                            <LiveValue xsi:type="xsd:string">1</LiveValue>
                          </anyType>
                        </value>
                      </item>
                    </CustomProperties>
                    <IndicatorHolder>
                      <IndicatorName>PriceLine</IndicatorName>
                      <Plots />
                    </IndicatorHolder>
                    <IsExplicitlyNamed>false</IsExplicitlyNamed>
                    <IsPriceTypeLocked>false</IsPriceTypeLocked>
                    <PlotOnChart>false</PlotOnChart>
                    <PriceType>Close</PriceType>
                    <SeriesType>Indicator</SeriesType>
                  </HostedDataSeries>
                </Series1>
                <StartBar>0</StartBar>
                <State>Undefined</State>
                <Time>0001-01-01T00:00:00</Time>
              </LeftItem>
              <Lookback>1</Lookback>
              <Operator>Equals</Operator>
              <RightItem xsi:type="WizardConditionItem">
                <Children />
                <IsExpanded>true</IsExpanded>
                <IsSelected>true</IsSelected>
                <Name>Close</Name>
                <OffsetType>Arithmetic</OffsetType>
                <AssignedCommand>
                  <Command>{0}</Command>
                  <Parameters>
                    <string>Series1</string>
                    <string>BarsAgo</string>
                    <string>OffsetBuilder</string>
                  </Parameters>
                </AssignedCommand>
                <BarsAgo>15</BarsAgo>
                <CurrencyType>Currency</CurrencyType>
                <Date>2019-12-21T16:04:34.8437282</Date>
                <DayOfWeek>Sunday</DayOfWeek>
                <EndBar>0</EndBar>
                <ForceSeriesIndex>false</ForceSeriesIndex>
                <LookBackPeriod>0</LookBackPeriod>
                <MarketPosition>Long</MarketPosition>
                <Period>0</Period>
                <ReturnType>Series</ReturnType>
                <Series1>
                  <AcceptableSeries>Indicator DataSeries CustomSeries DefaultSeries</AcceptableSeries>
                  <CustomProperties>
                    <item>
                      <key>
                        <string>ShowAskLine</string>
                      </key>
                      <value>
                        <anyType xsi:type="xsd:boolean">false</anyType>
                      </value>
                    </item>
                    <item>
                      <key>
                        <string>ShowBidLine</string>
                      </key>
                      <value>
                        <anyType xsi:type="xsd:boolean">false</anyType>
                      </value>
                    </item>
                    <item>
                      <key>
                        <string>ShowLastLine</string>
                      </key>
                      <value>
                        <anyType xsi:type="xsd:boolean">true</anyType>
                      </value>
                    </item>
                    <item>
                      <key>
                        <string>AskLineLength</string>
                      </key>
                      <value>
                        <anyType xsi:type="NumberBuilder">
                          <DefaultValue>0</DefaultValue>
                          <IsInt>true</IsInt>
                          <IsLiteral>true</IsLiteral>
                          <LiveValue xsi:type="xsd:string">100</LiveValue>
                        </anyType>
                      </value>
                    </item>
                    <item>
                      <key>
                        <string>BidLineLength</string>
                      </key>
                      <value>
                        <anyType xsi:type="NumberBuilder">
                          <DefaultValue>0</DefaultValue>
                          <IsInt>true</IsInt>
                          <IsLiteral>true</IsLiteral>
                          <LiveValue xsi:type="xsd:string">100</LiveValue>
                        </anyType>
                      </value>
                    </item>
                    <item>
                      <key>
                        <string>LastLineLength</string>
                      </key>
                      <value>
                        <anyType xsi:type="NumberBuilder">
                          <DefaultValue>0</DefaultValue>
                          <IsInt>true</IsInt>
                          <IsLiteral>true</IsLiteral>
                          <LiveValue xsi:type="xsd:string">100</LiveValue>
                        </anyType>
                      </value>
                    </item>
                  </CustomProperties>
                  <IndicatorHolder>
                    <IndicatorName>PriceLine</IndicatorName>
                    <Plots />
                  </IndicatorHolder>
                  <IsExplicitlyNamed>false</IsExplicitlyNamed>
                  <IsPriceTypeLocked>false</IsPriceTypeLocked>
                  <PlotOnChart>false</PlotOnChart>
                  <PriceType>Close</PriceType>
                  <SeriesType>Indicator</SeriesType>
                </Series1>
                <StartBar>0</StartBar>
                <State>Undefined</State>
                <Time>0001-01-01T00:00:00</Time>
              </RightItem>
            </WizardCondition>
          </Conditions>
          <IsGroup>false</IsGroup>
          <DisplayName>PriceLine(PriceLine(Close, false, false, true, 1, 1, 1), false, false, true, 100, 100, 100)[15] = PriceLine(Close, false, false, true, 100, 100, 100)[15]</DisplayName>
        </WizardConditionGroup>
      </Conditions>
      <SetName>Set 1</SetName>
      <SetNumber>1</SetNumber>
    </ConditionalAction>
  </ConditionalActions>
  <CustomSeries>
    <CustomSeriesProperties>
      <Name>Resistance</Name>
      <Type>Bool</Type>
      <SeriesID>f4619060-98af-4c92-9ca1-6a600702be18</SeriesID>
    </CustomSeriesProperties>
    <CustomSeriesProperties>
      <Name>Support</Name>
      <Type>Bool</Type>
      <SeriesID>4c9ba11c-8938-4c9a-829a-8cb44b8134a2</SeriesID>
    </CustomSeriesProperties>
  </CustomSeries>
  <DataSeries>
    <DataSeriesProperties>
      <InstrumentName>ES 12-19</InstrumentName>
      <PriceBasedOn>Last</PriceBasedOn>
      <SameAsPrimary>false</SameAsPrimary>
      <Type>Minute</Type>
      <Value>1</Value>
    </DataSeriesProperties>
  </DataSeries>
  <Description>Tring to make trends</Description>
  <DisplayInDataBox>true</DisplayInDataBox>
  <DrawHorizontalGridLines>true</DrawHorizontalGridLines>
  <DrawOnPricePanel>true</DrawOnPricePanel>
  <DrawVerticalGridLines>true</DrawVerticalGridLines>
  <EntriesPerDirection>20</EntriesPerDirection>
  <EntryHandling>UniqueEntries</EntryHandling>
  <ExitOnSessionClose>true</ExitOnSessionClose>
  <ExitOnSessionCloseSeconds>30</ExitOnSessionCloseSeconds>
  <FillLimitOrdersOnTouch>true</FillLimitOrdersOnTouch>
  <InputParameters>
    <InputParameter>
      <Default>1</Default>
      <Description />
      <Name>Price</Name>
      <Minimum>1</Minimum>
      <Type>int</Type>
    </InputParameter>
  </InputParameters>
  <IsTradingHoursBreakLineVisible>true</IsTradingHoursBreakLineVisible>
  <IsInstantiatedOnEachOptimizationIteration>true</IsInstantiatedOnEachOptimizationIteration>
  <MaximumBarsLookBack>TwoHundredFiftySix</MaximumBarsLookBack>
  <MinimumBarsRequired>20</MinimumBarsRequired>
  <OrderFillResolution>Standard</OrderFillResolution>
  <OrderFillResolutionValue>1</OrderFillResolutionValue>
  <OrderFillResolutionType>Minute</OrderFillResolutionType>
  <OverlayOnPrice>false</OverlayOnPrice>
  <PaintPriceMarkers>true</PaintPriceMarkers>
  <PlotParameters />
  <RealTimeErrorHandling>StopCancelClose</RealTimeErrorHandling>
  <ScaleJustification>Right</ScaleJustification>
  <ScriptType>Strategy</ScriptType>
  <Slippage>0</Slippage>
  <StartBehavior>WaitUntilFlat</StartBehavior>
  <StopsAndTargets>
    <WizardAction>
      <Children />
      <IsExpanded>false</IsExpanded>
      <IsSelected>true</IsSelected>
      <Name>Stop loss total position</Name>
      <OffsetType>Arithmetic</OffsetType>
      <ActionProperties>
        <DashStyle>Solid</DashStyle>
        <DivideTimePrice>false</DivideTimePrice>
        <Id />
        <File />
        <IsAutoScale>false</IsAutoScale>
        <IsSimulatedStop>false</IsSimulatedStop>
        <IsStop>false</IsStop>
        <LogLevel>Information</LogLevel>
        <Mode>Percent</Mode>
        <OffsetType>Currency</OffsetType>
        <Priority>Medium</Priority>
        <Quantity>
          <DefaultValue>0</DefaultValue>
          <IsInt>true</IsInt>
          <DynamicValue>
            <Children />
            <IsExpanded>false</IsExpanded>
            <IsSelected>false</IsSelected>
            <Name>Default order quantity</Name>
            <OffsetType>Arithmetic</OffsetType>
            <AssignedCommand>
              <Command>DefaultQuantity</Command>
              <Parameters />
            </AssignedCommand>
            <BarsAgo>0</BarsAgo>
            <CurrencyType>Currency</CurrencyType>
            <Date>2019-12-21T17:31:36.1507005</Date>
            <DayOfWeek>Sunday</DayOfWeek>
            <EndBar>0</EndBar>
            <ForceSeriesIndex>false</ForceSeriesIndex>
            <LookBackPeriod>0</LookBackPeriod>
            <MarketPosition>Long</MarketPosition>
            <Period>0</Period>
            <ReturnType>Number</ReturnType>
            <StartBar>0</StartBar>
            <State>Undefined</State>
            <Time>0001-01-01T00:00:00</Time>
          </DynamicValue>
          <IsLiteral>false</IsLiteral>
          <LiveValue xsi:type="xsd:string">DefaultQuantity</LiveValue>
        </Quantity>
        <ServiceName />
        <ScreenshotPath />
        <SoundLocation />
        <Tag>
          <SeparatorCharacter> </SeparatorCharacter>
          <Strings>
            <NinjaScriptString>
              <Index>0</Index>
              <StringValue>Set Stop loss total position</StringValue>
            </NinjaScriptString>
          </Strings>
        </Tag>
        <TextPosition>BottomLeft</TextPosition>
        <Value>
          <DefaultValue>0</DefaultValue>
          <IsInt>false</IsInt>
          <IsLiteral>true</IsLiteral>
          <LiveValue xsi:type="xsd:string">3</LiveValue>
        </Value>
        <VariableDateTime>2019-12-21T17:31:36.1507005</VariableDateTime>
        <VariableBool>false</VariableBool>
      </ActionProperties>
      <ActionType>Misc</ActionType>
      <Command>
        <Command>SetStopLoss</Command>
        <Parameters>
          <string>mode</string>
          <string>value</string>
        </Parameters>
      </Command>
    </WizardAction>
  </StopsAndTargets>
  <StopTargetHandling>ByStrategyPosition</StopTargetHandling>
  <TimeInForce>Day</TimeInForce>
  <TraceOrders>false</TraceOrders>
  <UseOnAddTradeEvent>false</UseOnAddTradeEvent>
  <UseOnAuthorizeAccountEvent>false</UseOnAuthorizeAccountEvent>
  <UseAccountItemUpdate>false</UseAccountItemUpdate>
  <UseOnCalculatePerformanceValuesEvent>true</UseOnCalculatePerformanceValuesEvent>
  <UseOnConnectionEvent>false</UseOnConnectionEvent>
  <UseOnDataPointEvent>true</UseOnDataPointEvent>
  <UseOnFundamentalDataEvent>false</UseOnFundamentalDataEvent>
  <UseOnExecutionEvent>false</UseOnExecutionEvent>
  <UseOnMouseDown>true</UseOnMouseDown>
  <UseOnMouseMove>true</UseOnMouseMove>
  <UseOnMouseUp>true</UseOnMouseUp>
  <UseOnMarketDataEvent>false</UseOnMarketDataEvent>
  <UseOnMarketDepthEvent>false</UseOnMarketDepthEvent>
  <UseOnMergePerformanceMetricEvent>false</UseOnMergePerformanceMetricEvent>
  <UseOnNextDataPointEvent>true</UseOnNextDataPointEvent>
  <UseOnNextInstrumentEvent>true</UseOnNextInstrumentEvent>
  <UseOnOptimizeEvent>true</UseOnOptimizeEvent>
  <UseOnOrderUpdateEvent>false</UseOnOrderUpdateEvent>
  <UseOnPositionUpdateEvent>false</UseOnPositionUpdateEvent>
  <UseOnRenderEvent>true</UseOnRenderEvent>
  <UseOnRestoreValuesEvent>false</UseOnRestoreValuesEvent>
  <UseOnShareEvent>true</UseOnShareEvent>
  <UseOnWindowCreatedEvent>false</UseOnWindowCreatedEvent>
  <UseOnWindowDestroyedEvent>false</UseOnWindowDestroyedEvent>
  <Variables />
  <Name>GeorgeClooney</Name>
</ScriptProperties>
@*/
#endregion
