import javascript
import DataFlow::PathGraph

class VscodeXssConfiguration extends TaintTracking::Configuration {
  VscodeXssConfiguration() { this = "VscodeXssConfiguration" }
  
  override predicate isSource(DataFlow::Node source) {
    // Define sources - places where untrusted data enters
    exists(source.asExpr().(Parameter)) or
    source instanceof RemoteFlowSource
  }
  
  override predicate isSink(DataFlow::Node sink) {
    // Define sinks - dangerous places where data is used
    exists(MethodCallExpr call |
      call.getMethodName() = "setHtml" and
      sink.asExpr() = call.getArgument(0)
    )
  }
}

from VscodeXssConfiguration config, DataFlow::PathNode source, DataFlow::PathNode sink
where config.hasFlowPath(source, sink)
select sink, source, sink, "Potential XSS vulnerability due to unvalidated data flow"