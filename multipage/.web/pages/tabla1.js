/** @jsxImportSource @emotion/react */


import { ErrorBoundary } from "react-error-boundary"
import { Fragment, useContext, useEffect, useState } from "react"
import { ColorModeContext, EventLoopContext, StateContexts } from "/utils/context"
import { Event, getBackendURL, isTrue, refs } from "/utils/state"
import { WifiOffIcon as LucideWifiOffIcon } from "lucide-react"
import { keyframes } from "@emotion/react"
import { toast, Toaster } from "sonner"
import env from "/env.json"
import { Box as RadixThemesBox, Heading as RadixThemesHeading, Table as RadixThemesTable } from "@radix-ui/themes"
import NextHead from "next/head"



                function Fallback({ error, resetErrorBoundary }) {
                    return (
                        <div>
  <p>
  {"Ooops...Unknown Reflex error has occured:"}
</p>
  <p css={({ ["color"] : "red" })}>
  {error.message}
</p>
  <p>
  {"Please contact the support."}
</p>
</div>
                    );
                }
            

export function Fragment_e521b13e556da291bcec5187a783ea81 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <Fragment>
  {isTrue((connectErrors.length > 0)) ? (
  <Fragment>
  <LucideWifiOffIcon css={({ ["color"] : "crimson", ["zIndex"] : 9999, ["position"] : "fixed", ["bottom"] : "33px", ["right"] : "33px", ["animation"] : (pulse+" 1s infinite") })} size={32}/>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

const pulse = keyframes`
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
`


export function Table__row_e737279f49c03f3081306664fa0dabac () {
  const reflex___state____state__mp___pages___tabla1____data = useContext(StateContexts.reflex___state____state__mp___pages___tabla1____data)



  return (
    <RadixThemesTable.Row>
  <>{reflex___state____state__mp___pages___tabla1____data.cabecera.map((x, index_51a84561ff0be13b) => (
  <RadixThemesTable.ColumnHeaderCell key={index_51a84561ff0be13b}>
  {x}
</RadixThemesTable.ColumnHeaderCell>
))}</>
</RadixThemesTable.Row>
  )
}

export function Toaster_9d6e054b03c6e5d1bea1c0a5576b4e6d () {
  const { resolvedColorMode } = useContext(ColorModeContext)


  refs['__toast'] = toast
  const [addEvents, connectErrors] = useContext(EventLoopContext);
  const toast_props = ({ ["description"] : ("Check if server is reachable at "+getBackendURL(env.EVENT).href), ["closeButton"] : true, ["duration"] : 120000, ["id"] : "websocket-error" });
  const [userDismissed, setUserDismissed] = useState(false);
  (useEffect(
() => {
    if ((connectErrors.length >= 2)) {
        if (!userDismissed) {
            toast.error(
                `Cannot connect to server: ${((connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : '')}.`,
                {...toast_props, onDismiss: () => setUserDismissed(true)},
            )
        }
    } else {
        toast.dismiss("websocket-error");
        setUserDismissed(false);  // after reconnection reset dismissed state
    }
}
, [connectErrors]))

  return (
    <Toaster closeButton={false} expand={true} position={"bottom-right"} richColors={true} theme={resolvedColorMode}/>
  )
}

export function Div_24a2e81d0c5d3cb5b5f786fdef44e514 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <div css={({ ["position"] : "fixed", ["width"] : "100vw", ["height"] : "0" })} title={("Connection Error: "+((connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : ''))}>
  <Fragment_e521b13e556da291bcec5187a783ea81/>
</div>
  )
}

export function Table__body_fe624f414e9c88029f8c747258622d12 () {
  const reflex___state____state__mp___pages___tabla1____data = useContext(StateContexts.reflex___state____state__mp___pages___tabla1____data)



  return (
    <RadixThemesTable.Body>
  <>{reflex___state____state__mp___pages___tabla1____data.gente.map((record, index_01c3cd18b9be7798) => (
  <RadixThemesTable.Row key={index_01c3cd18b9be7798}>
  <>{record.map((x, index_81089840465cb7cc) => (
  <RadixThemesTable.Cell key={index_81089840465cb7cc}>
  {x}
</RadixThemesTable.Cell>
))}</>
</RadixThemesTable.Row>
))}</>
</RadixThemesTable.Body>
  )
}

export default function Component() {
  const [addEvents, connectErrors] = useContext(EventLoopContext);
  
    const logFrontendError = (error, info) => {
        if (process.env.NODE_ENV === "production") {
            addEvents([Event("reflex___state____state.reflex___state____frontend_event_exception_state.handle_frontend_exception", {
                stack: error.stack,
            })])
        }
    }
    

  return (
    <ErrorBoundary FallbackComponent={Fallback} onError={logFrontendError}>
  <Fragment>
  <Div_24a2e81d0c5d3cb5b5f786fdef44e514/>
  <Toaster_9d6e054b03c6e5d1bea1c0a5576b4e6d/>
</Fragment>
  <RadixThemesBox>
  <RadixThemesHeading align={"center"}>
  {"Tabla de Datos"}
</RadixThemesHeading>
  <RadixThemesTable.Root>
  <RadixThemesTable.Header>
  <Table__row_e737279f49c03f3081306664fa0dabac/>
</RadixThemesTable.Header>
  <Table__body_fe624f414e9c88029f8c747258622d12/>
</RadixThemesTable.Root>
</RadixThemesBox>
  <NextHead>
  <title>
  {"Mp | Tabla1"}
</title>
  <meta content={"favicon.ico"} property={"og:image"}/>
</NextHead>
</ErrorBoundary>
  )
}